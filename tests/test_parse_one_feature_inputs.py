import email_mbmlbook
import pandas as pd
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
