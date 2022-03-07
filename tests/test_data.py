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
