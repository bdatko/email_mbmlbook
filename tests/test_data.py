import email_mbmlbook
import pytest


class TestOneFeatureInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OneFeatureInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def single(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, single):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, single):
        # Arrange
        # Act
        # Assert
        assert (4657, 4) == single.shape

    @pytest.mark.parametrize(
        "column,expected",
        [
            ("user", ["User35CB8E5"]),
            ("dataset", ["Train", "Validation", "Test"]),
            ("ToLine", [1, 0]),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, single):
        # Arrange
        # Act
        unique_val = single[column].unique()
        # Assert
        assert sorted(unique_val) == sorted(expected)

    @pytest.mark.parametrize(
        "column,expected",
        [
            ("user", {"User35CB8E5": 4657}),
            ("dataset", {"Validation": 2005, "Train": 1995, "Test": 657}),
            ("ToLine", {0: 3597, 1: 1060}),
            ("repliedTo", {False: 4517, True: 140}),
        ],
    )
    def test_dist_values(self, column, expected, single):
        # Arrange
        # Act
        dist = single[column].value_counts().to_dict()
        # Assert
        assert dist == expected


class TestCompoundInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/CompoundInputs.objml"
    DATASETS = ["Train", "Validation", "TrainAndValidation"]

    @pytest.fixture
    def compound(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, compound):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, compound):
        # Arrange
        # Act
        # Assert
        assert (9000, 6) == compound.shape

    @pytest.mark.parametrize(
        "column,expected",
        [
            ("user", ["User35CB8E5"]),
            ("dataset", ["Train", "TrainAndValidation", "Validation"]),
            ("ToLine", [0, 1]),
            ("FromManager", [0, 1]),
            ("And", [0, 1]),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, compound):
        # Arrange
        # Act
        unique_val = compound[column].unique()
        # Assert
        assert sorted(unique_val) == sorted(expected)

    @pytest.mark.parametrize(
        "column,expected",
        [
            ("user", {"User35CB8E5": 9000}),
            (
                "dataset",
                {"TrainAndValidation": 4500, "Validation": 2255, "Train": 2245},
            ),
            ("ToLine", {0: 6630, 1: 2370}),
            ("FromManager", {0: 8000, 1: 1000}),
            ("And", {0: 8500, 1: 500}),
            ("repliedTo", {False: 8336, True: 664}),
        ],
    )
    def test_dist_values(self, column, expected, compound):
        # Arrange
        # Act
        dist = compound[column].value_counts().to_dict()
        # Assert
        assert dist == expected


class TestInitialInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/InitialInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def initial(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, initial):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, initial):
        # Arrange
        # Act
        # Assert
        assert (27942, 9) == initial.shape

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
            ("FromMe", [0, 1]),
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
            ("HasAttachments", [0, 1]),
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
            ("Sender", 3397),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, initial):
        # Arrange
        # Act
        unique_val = initial[column].unique()
        # Assert
        if column == "Sender":
            assert initial[column].unique().shape[0] == expected
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
            ("Sender", 3397),
            ("repliedTo", {False: 25766, True: 2176}),
        ],
    )
    def test_dist_values(self, column, expected, initial):
        # Arrange
        # Act
        dist = initial[column].value_counts().to_dict()
        # Assert
        if column == "Sender":
            assert initial[column].unique().shape[0] == expected
        else:
            assert dist == expected


class TestOfflineInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OfflineInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def offline(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, offline):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, offline):
        # Arrange
        # Act
        # Assert
        assert (27942, 11) == offline.shape

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
            ("FromMe", [0, 1]),
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
            ("HasAttachments", [0, 1]),
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
            ("Sender", 3397),
            ("Recipient", 9484),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, offline):
        # Arrange
        # Act
        unique_val = offline[column].unique()
        # Assert
        if column == "Sender":
            assert offline[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert offline[column].unique().shape[0] == expected
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
            ("Sender", 3397),
            ("Recipient", 9484),
            ("repliedTo", {False: 25766, True: 2176}),
        ],
    )
    def test_dist_values(self, column, expected, offline):
        # Arrange
        # Act
        dist = offline[column].value_counts().to_dict()
        # Assert
        if column == "Sender":
            assert offline[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert offline[column].unique().shape[0] == expected
        else:
            assert dist == expected


class TestSeperateInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/SeparateInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def seperate(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, seperate):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, seperate):
        # Arrange
        # Act
        # Assert
        assert (5157, 5) == seperate.shape

    @pytest.mark.parametrize(
        "column,expected",
        [
            (
                "user",
                [
                    "User35CB8E5",
                ],
            ),
            ("dataset", ["Train", "Validation", "Test"]),
            ("ToLine", [1.0, 0.0]),
            (
                "FromManager",
                [0.0, 1.0],
            ),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, seperate):
        # Arrange
        # Act
        unique_val = seperate[column].unique()
        # Assert
        assert sorted(unique_val) == sorted(expected)

    @pytest.mark.parametrize(
        "column,expected",
        [
            (
                "user",
                {
                    "User35CB8E5": 5157,
                },
            ),
            (
                "dataset",
                {"Train": 2245, "Validation": 2255, "Test": 657},
            ),
            ("ToLine", {0.0: 3847, 1.0: 1310}),
            ("FromManager", {0.0: 4657, 1.0: 500}),
            ("repliedTo", {False: 4815, True: 342}),
        ],
    )
    def test_dist_values(self, column, expected, seperate):
        # Arrange
        # Act
        dist = seperate[column].value_counts().to_dict()
        # Assert
        assert dist == expected


class TestWithRecipient:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/WithRecipientInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def with_recipient(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, with_recipient):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, with_recipient):
        # Arrange
        # Act
        # Assert
        assert (27942, 11) == with_recipient.shape

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
            ("Sender", 3397),
            ("Recipient", 9484),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, with_recipient):
        # Arrange
        # Act
        unique_val = with_recipient[column].unique()
        # Assert
        if column == "Sender":
            assert with_recipient[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert with_recipient[column].unique().shape[0] == expected
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
            ("Sender", 3397),
            ("Recipient", 9484),
            ("repliedTo", {False: 25766, True: 2176}),
        ],
    )
    def test_dist_values(self, column, expected, with_recipient):
        # Arrange
        # Act
        dist = with_recipient[column].value_counts().to_dict()
        # Assert
        if column == "Sender":
            assert with_recipient[column].unique().shape[0] == expected
        elif column == "Recipient":
            assert with_recipient[column].unique().shape[0] == expected
        else:
            assert dist == expected


class TestWithSubjectPrefix:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/WithSubjectPrefixInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]

    @pytest.fixture
    def with_subject_recipient(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(self.XML, self.DATASETS)
        return one_feature_inputs.to_pandas()

    def test_smoke(self, with_subject_recipient):
        # Arrange
        # Act
        # Assert
        assert True

    def test_shape(self, with_subject_recipient):
        # Arrange
        # Act
        # Assert
        assert (27942, 10) == with_subject_recipient.shape

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
            ("Sender", 3397),
            ("repliedTo", [False, True]),
        ],
    )
    def test_unique(self, column, expected, with_subject_recipient):
        # Arrange
        # Act
        unique_val = with_subject_recipient[column].unique()
        # Assert
        if column == "Sender":
            assert with_subject_recipient[column].unique().shape[0] == expected
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
            ("Sender", 3397),
            ("repliedTo", {False: 25766, True: 2176}),
        ],
    )
    def test_dist_values(self, column, expected, with_subject_recipient):
        # Arrange
        # Act
        dist = with_subject_recipient[column].value_counts().to_dict()
        # Assert
        if column == "Sender":
            assert with_subject_recipient[column].unique().shape[0] == expected
        else:
            assert dist == expected
