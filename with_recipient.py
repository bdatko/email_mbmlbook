import email_mbmlbook


XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/WithRecipientInputs.objml"

with_recipient = email_mbmlbook.FeatureSet(
    XML,
    ["Train", "Validation", "Test"],
)

res = with_recipient.to_pandas()
print(res.shape)
