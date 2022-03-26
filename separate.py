import email_mbmlbook

XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/SeparateInputs.objml"

separate = email_mbmlbook.FeatureSet(
    XML,
    ["Train", "Validation", "Test"],
)

res = separate.to_pandas()
print(res.shape)
