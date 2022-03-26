import email_mbmlbook


XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OfflineInputs.objml"

offline = email_mbmlbook.FeatureSet(
    XML,
    ["Train", "Validation", "Test"],
)

res = offline.to_pandas()
print(res.shape)
