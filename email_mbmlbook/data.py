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
    features: list

    def __post_init__(self):
        self.tree = untangle.parse(self.xml)
        self.base = "InputsCollection.Inputs.Inputs"
        self.columns = ["user", "dataset"] + self.features + ["repliedTo"]
        self.source = {
            dataset: self.base + f".{dataset}.Instances.Instance"
            for dataset in self.datasets
        }

    @property
    def user(self):
        return attrgetter("InputsCollection.Inputs.Inputs")(self.tree).get_attribute(
            "UserName"
        )

    def insert(self, dataset):
        return f".{dataset}.".join(self.base.rsplit("..", 1))

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
