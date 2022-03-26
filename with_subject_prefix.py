import email_mbmlbook


XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/WithSubjectPrefixInputs.objml"

with_subject_prefix = email_mbmlbook.FeatureSet(
    XML,
    ["Train", "Validation", "Test"],
)

res = with_subject_prefix.to_pandas()
print(res.shape)
