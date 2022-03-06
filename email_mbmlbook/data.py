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
        self.base = "InputsCollection.Inputs.Inputs..Instances.Instance"
        self.columns = ["user", "dataset"] + self.features + ["repliedTo"]
        self.source = {dataset: self.insert(dataset) for dataset in self.datasets}

    @property
    def user(self):
        return attrgetter("InputsCollection.Inputs.Inputs")(self.tree).get_attribute(
            "UserName"
        )

    def insert(self, dataset):
        return f".{dataset}.".join(self.base.rsplit("..", 1))

    def to_pandas(self):
        data = []
        for dataset, path in self.source.items():
            for item in attrgetter(path)(self.tree):
                features = list(map(int, [f.cdata for f in item.FeatureValues.Double]))
                repliedTo = True if item.get_attribute("Label") else False
                row = tuple([self.user, dataset] + features + [repliedTo])
                data.append(row)

        return pd.DataFrame(data, columns=self.columns)
