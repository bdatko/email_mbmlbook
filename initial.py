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
        self.categories = self._cardinality()
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

    def _cardinality(self):
        _maps = {}
        for user_input in attrgetter(self.base)(self.tree):
            user = user_input.get_attribute("UserName")
            _maps[user] = {}
            for feature in user_input.FeatureSet.Features.get_elements():
                # _maps[user][feature._name]
                codex = {
                    feature_bucket.get_attribute("x:id"): feature_bucket.get_attribute(
                        "Name"
                    )
                    for feature_bucket in feature.get_elements(name="Buckets")[
                        0
                    ].get_elements()
                }
                _maps[user][feature._name] = codex

        return _maps

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
                    for feature, ref, double in zip(
                        self.features,
                        instance.get_elements("FeatureValues")[0].x_key,
                        instance.get_elements("FeatureValues")[0].Double,
                    ):
                        if len(self.categories[user][feature]) > 1:
                            row.append(
                                self.categories[user][feature][
                                    ref.get_attribute("x:idref")
                                ]
                            )
                        elif len(self.categories[user][feature]) == 1:
                            row.append(int(double.cdata))
                    row.append(repliedTo)
                    row = tuple(row)
                    data.append(row)

        return pd.DataFrame(data, columns=self.columns)


XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/InitialInputs.objml"

initial = FeatureSet(XML, ["Train", "Validation", "Test"])
res = initial._cardinality()
res = initial.to_pandas()

# compound_input = FeatureSet(
#     XML,
#     [
#         "Train",
#         "Validation",
#     ],
#     ["ToLine", "FromManager", "And"],
# )

# compound = compound_input.to_pandsa()

# o = untangle.parse(XML)
