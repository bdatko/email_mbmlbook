"""
Classes for Data Objects
"""

from dataclasses import dataclass
from operator import attrgetter

import pandas as pd
import untangle


@dataclass
class FeatureSet:
    xml: str
    datasets: list

    def __post_init__(self):
        self.tree = untangle.parse(self.xml)
        self.base = "InputsCollection.Inputs.Inputs"
        self.features = self._validate_features()
        self.columns = ["user", "dataset"] + self.features + ["repliedTo"]
        self.source = {
            dataset: self.base + f".{dataset}.Instances.Instance"
            for dataset in self.datasets
        }

    def _validate_features(self):
        _features = []
        for user_input in attrgetter(self.base)(self.tree):
            features = [
                item._name for item in user_input.FeatureSet.Features.get_elements()
            ]
            _features.append(features)

        if any(element != _features[0] for element in _features):
            raise ValueError("FeatureSet are different accross users")

        return _features[0]

    def to_pandas(self):
        data = []
        for user_input in attrgetter(self.base)(self.tree):
            user = user_input.get_attribute("UserName")
            for dataset, path in self.source.items():
                for item in attrgetter(path)(self.tree):
                    features = list(
                        map(int, [f.cdata for f in item.FeatureValues.Double])
                    )
                    repliedTo = True if item.get_attribute("Label") else False
                    row = tuple([user, dataset] + features + [repliedTo])
                    data.append(row)

        return pd.DataFrame(data, columns=self.columns)
