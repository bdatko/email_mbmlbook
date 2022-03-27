import email_mbmlbook
import pandas as pd
import pytest


class TestPersonalisationInputs:

    XML = [
        "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/Personalisation1Inputs.objml",
        "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/Personalisation2Inputs.objml",
    ]
    user_feature_set_reference = ["User35CB8E5", "User223AECA"]
    DATASETS = ["Train", "Validation", "Test"]
    SOURCE = "data/PersonalisationInputs_objml.csv"

    @pytest.fixture
    def personalisation(self):
        return pd.read_csv(self.SOURCE)

    def test_smoke(self, personalisation):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, personalisation):
        # Arrange
        # Act
        # Assert
        assert (27942, 12) == personalisation.shape

    @pytest.mark.parametrize(
        "column,expected",
        [
            (
                "user",
                [
                    "User35CB8E5",
                    "UserCE3FDB4",
                    "User6AACED",
                    "User7E601F9",
                    "User68251CD",
                    "User223AECA",
                    "UserFF0F29E",
                    "User25C0488",
                    "User811E39F",
                    "User10628A6",
                ],
            ),
            ("dataset", ["Train", "Validation", "Test"]),
            ("FromMe", [0.0, 1.0]),
            (
                "ToCcPosition",
                [
                    "FirstOnToLine",
                    "NotOnToOrCcLine",
                    "FirstOnCcLine",
                    "SecondOrLaterOnCcLine",
                    "SecondOnToLine",
                    "ThirdOrLaterOnToLine",
                ],
            ),
            ("HasAttachments", [0.0, 1.0]),
            (
                "BodyLength",
                [
                    ">1023",
                    "129-256",
                    "513-1023",
                    "33-64",
                    "257-512",
                    "17-32",
                    "65-128",
                    "9-16",
                    "0",
                    "5-8",
                    "1-4",
                ],
            ),
            (
                "SubjectLength",
                ["33-64", "17-32", ">64", "9-16", "5-8", "3-4", "0", "1-2"],
            ),
            ("SubjectPrefix", ["no prefix", "re", "Other", "fw"]),
            ("Bias", [-3.1622776601683795]),
            ("Sender", 3397),
            ("Recipient", 8216),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, personalisation):
        # Arrange
        # Act
        unique_val = personalisation[column].unique()
        # Assert
        if column == "Sender":
            assert personalisation[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert personalisation[column].unique().shape[0] == expected
        else:
            assert sorted(unique_val) == sorted(expected)

    @pytest.mark.parametrize(
        "column,expected",
        [
            (
                "user",
                {
                    "UserFF0F29E": 5130,
                    "User35CB8E5": 4657,
                    "User6AACED": 4249,
                    "User811E39F": 3652,
                    "User25C0488": 2756,
                    "UserCE3FDB4": 2490,
                    "User68251CD": 1400,
                    "User223AECA": 1243,
                    "User7E601F9": 1232,
                    "User10628A6": 1133,
                },
            ),
            (
                "dataset",
                {"Train": 11994, "Validation": 11987, "Test": 3961},
            ),
            ("FromMe", {0: 27287, 1: 655}),
            (
                "ToCcPosition",
                {
                    "NotOnToOrCcLine": 16147,
                    "FirstOnToLine": 7950,
                    "SecondOnToLine": 1207,
                    "ThirdOrLaterOnToLine": 1112,
                    "FirstOnCcLine": 792,
                    "SecondOrLaterOnCcLine": 734,
                },
            ),
            ("HasAttachments", {0: 26245, 1: 1697}),
            (
                "BodyLength",
                {
                    "513-1023": 7276,
                    ">1023": 6966,
                    "257-512": 4557,
                    "129-256": 3781,
                    "65-128": 2647,
                    "33-64": 1399,
                    "17-32": 640,
                    "9-16": 275,
                    "5-8": 163,
                    "0": 128,
                    "1-4": 110,
                },
            ),
            (
                "SubjectLength",
                {
                    "33-64": 11321,
                    "17-32": 8810,
                    ">64": 4321,
                    "9-16": 2730,
                    "5-8": 542,
                    "3-4": 142,
                    "0": 55,
                    "1-2": 21,
                },
            ),
            (
                "SubjectPrefix",
                {"no prefix": 13623, "re": 13312, "Other": 198, "fw": 809},
            ),
            ("Bias", {-3.1622776601683795: 27942}),
            ("Sender", 3397),
            ("Recipient", 8216),
            ("repliedTo", {False: 25766, True: 2176}),
        ],
    )
    def test_dist_values(self, column, expected, personalisation):
        # Arrange
        # Act
        dist = personalisation[column].value_counts().to_dict()
        # Assert
        if column == "Sender":
            assert personalisation[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert personalisation[column].unique().shape[0] == expected
        else:
            assert dist == expected
