import email_mbmlbook
import pandas as pd


XML01 = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/Personalisation1Inputs.objml"
XML02 = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/Personalisation2Inputs.objml"

personalisation01 = email_mbmlbook.FeatureSet(
    XML01, ["Train", "Validation", "Test"], user_feature_set="User35CB8E5"
)

personalisation02 = email_mbmlbook.FeatureSet(
    XML02, ["Train", "Validation", "Test"], user_feature_set="User223AECA"
)

res01 = personalisation01.to_pandas()
res02 = personalisation02.to_pandas()
print(res01.shape)
print(res02.shape)

res = pd.concat([res01, res02])
res.reset_index(inplace=True, drop=True)
