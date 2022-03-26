"""
Classes for Data Objects
"""

from dataclasses import dataclass
from itertools import zip_longest
from operator import attrgetter
from typing import Union

import numpy as np
import pandas as pd
import untangle
from more_itertools import peekable
from untangle import Element
from typing import Optional


@dataclass
class FeatureSet:
    xml: str
    datasets: list
    user_feature_set: Optional[str] = None

    def __post_init__(self):
        self.tree = untangle.parse(self.xml)
        self.base = "InputsCollection.Inputs.Inputs"
        self.features = self._validate_features()
        self.columns = ["user", "dataset"] + self.features + ["repliedTo"]
        self.categories = self._cardinality()
        self.source = {
            dataset: self.base + f".{dataset}.Instances.Instance"
            for dataset in self.datasets
        }

    def _validate_features(self):
        _features = []
        for user_input in attrgetter(self.base)(self.tree):
            if hasattr(user_input.FeatureSet, "Features"):
                features = [
                    item._name for item in user_input.FeatureSet.Features.get_elements()
                ]
            else:
                features = []
            _features.append(features)

        if self.user_feature_set is None:
            if any(element != _features[0] for element in _features):
                raise ValueError("FeatureSet are different accross users")

        return _features[0]

    def _cardinality(self):
        _maps = {}
        for user_input in attrgetter(self.base)(self.tree):
            user = user_input.get_attribute("UserName")
            _maps[user] = {}
            if hasattr(user_input.FeatureSet, "Features"):
                for feature in user_input.FeatureSet.Features.get_elements():
                    # _maps[user][feature._name]
                    codex = {
                        feature_bucket.get_attribute(
                            "x:id"
                        ): feature_bucket.get_attribute("Name")
                        for feature_bucket in feature.get_elements(name="Buckets")[
                            0
                        ].get_elements()
                    }
                    _maps[user][feature._name] = codex

        if self.user_feature_set is not None:
            for user in set(_maps.keys()) - set([self.user_feature_set]):
                orig = _maps[user].copy()
                _maps[user].update(_maps[self.user_feature_set].copy())
                _maps[user].update(orig)

        return _maps

    def _get_value(
        self, user: str, feature: str, ref: str, double: float
    ) -> Union[str, float]:
        """
        Returns either the double or mapped ref after determining if the feature
        has a boolan or categorical (cat > 2) domain
        """
        if len(self.categories[user][feature]) > 1:
            return self.categories[user][feature][ref]
        elif len(self.categories[user][feature]) == 1:
            return double

    def _parse_values(self, user: str, instance: Element) -> list:
        """
        Parse values from an instance
        when len(instance.get_elements()) == len(features)
        """
        values = []
        for feature, ref, double in zip(
            self.features,
            instance.get_elements("FeatureValues")[0].x_key,
            instance.get_elements("FeatureValues")[0].Double,
        ):
            if len(self.categories[user][feature]) > 1:
                values.append(
                    self.categories[user][feature][ref.get_attribute("x:idref")]
                )
            elif len(self.categories[user][feature]) == 1:
                values.append(float(double.cdata))

        return values

    def _parse_missing_values(self, user: str, instance: Element) -> list:
        """
        Parse values from an instance
        when len(instance.get_elements()) < len(features)
        - First, find what is missing
        - Second, parse normally using `parse_values`
        - Thrid, insert None into missing values
        """
        missing = []
        for element in instance.get_elements("FeatureValues")[0].x_key:
            ref = element.get_attribute("x:idref")
            missing.append([ref in self.categories[user][f] for f in self.features])
        missing = np.array(missing)
        missing_index = np.argwhere(np.all(~missing, axis=0) == True).flatten().tolist()
        values = self._parse_values(user, instance)
        for index in missing_index:
            values.insert(index, None)

        return values

    def _parse_list_values(self, user: str, instance: Element) -> list:
        values = []
        refs = [
            element.get_attribute("x:idref")
            for element in instance.get_elements("FeatureValues")[0].x_key
        ]
        doubles = [
            float(element.cdata)
            for element in instance.get_elements("FeatureValues")[0].Double
        ]
        features = self.features[:]
        it_f = peekable(features)
        it_d = peekable(doubles)
        multiples = []
        for feature, ref, double in zip_longest(it_f, refs, it_d):
            if not self._check_pos_float(double):
                values.append(self._get_value(user, feature, ref, float(double)))
                continue

            if self._check_pos_float(double):
                multiples.append(self._get_value(user, feature, ref, double))
                if self._check_pos_float(it_d.peek(1)):
                    it_f.prepend(feature)
                else:
                    values.append(";".join(sorted(multiples)))
                    multiples = []

        return values

    def _check_pos_float(self, num: float) -> bool:
        return num < 1 and num > 0

    def to_pandas(self):
        data = []
        for user_input in attrgetter(self.base)(self.tree):
            user = user_input.get_attribute("UserName")
            for dataset in self.datasets:
                for instance in (
                    user_input.get_elements(dataset)[0]
                    .get_elements("Instances")[0]
                    .get_elements()
                ):
                    repliedTo = True if instance.get_attribute("Label") else False
                    row = []
                    row.extend([user, dataset])
                    if len(self.features) * 2 == len(
                        instance.get_elements("FeatureValues")[0]
                    ):
                        values = self._parse_values(user, instance)
                    elif len(self.features) * 2 > len(
                        instance.get_elements("FeatureValues")[0]
                    ):
                        values = self._parse_missing_values(user, instance)
                    elif len(self.features) * 2 < len(
                        instance.get_elements("FeatureValues")[0]
                    ):
                        values = self._parse_list_values(user, instance)
                    row.extend(values)
                    row.append(repliedTo)
                    row = tuple(row)
                    data.append(row)

        return pd.DataFrame(data, columns=self.columns)
