from dataclasses import dataclass
from operator import attrgetter

import pandas as pd
import untangle


@dataclass
class FeatureSet:
    xml: str

    def __post_init__(self):
        self.tree = untangle.parse(self.xml)
        self.source = {
            "Train": "InputsCollection.Inputs.Inputs.Train.Instances.Instance",
            "Validation": "InputsCollection.Inputs.Inputs.Validation.Instances.Instance",
            "Test": "InputsCollection.Inputs.Inputs.Test.Instances.Instance",
        }
        self.columns = ["user", "dataset", "ToLine", "repliedTo"]

    @property
    def user(self):
        return attrgetter("InputsCollection.Inputs.Inputs")(self.tree).get_attribute(
            "UserName"
        )

    def to_pandsa(self):
        data = []
        for dataset, path in self.source.items():
            for item in attrgetter(path)(self.tree):
                ToLine = int(item.FeatureValues.Double.cdata)
                repliedTo = True if item.get_attribute("Label") else False
                data.append((self.user, dataset, ToLine, repliedTo))

        return pd.DataFrame(data, columns=self.columns)


one_feature_inputs = FeatureSet(
    "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OneFeatureInputs.objml"
)

single = one_feature_inputs.to_pandsa()

# mapping of dataest to attr
# mapping = {
#     "Train": "InputsCollection.Inputs.Inputs.Train.Instances.Instance",
#     "Validation": "",
#     "Test": "",
# }

# XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OneFeatureInputs.objml"

# o = untangle.parse(XML)

# user = o.InputsCollection.Inputs.Inputs.get_attribute("UserName")

# data = []

# for item in attrgetter(mapping["Train"])(o):
#     ToLine = int(item.FeatureValues.Double.cdata)
#     repliedTo = True if item.get_attribute("Label") else False
#     data.append((user, ref, "Train", ToLine, repliedTo))
