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

    def to_pandsa(self):
        data = []
        for dataset, path in self.source.items():
            for item in attrgetter(path)(self.tree):
                features = list(map(int, [f.cdata for f in item.FeatureValues.Double]))
                repliedTo = True if item.get_attribute("Label") else False
                row = tuple([self.user, dataset] + features + [repliedTo])
                data.append(row)

        return pd.DataFrame(data, columns=self.columns)


XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/CompoundInputs.objml"

compound_input = FeatureSet(
    XML, ["Train", "Validation", "TrainAndValidation"], ["ToLine", "FromManager", "And"]
)

compound = compound_input.to_pandsa()


o = untangle.parse(XML)

mapping = {"Train": "InputsCollection.Inputs.Inputs.Train.Instances.Instance"}

data = []

for item in attrgetter(mapping["Train"])(o):
    pass
    # ToLine = int(item.FeatureValues.Double.cdata)
    # repliedTo = True if item.get_attribute("Label") else False
    # data.append((user, ref, "Train", ToLine, repliedTo))
