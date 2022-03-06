import email_mbmlbook
import pytest


class TestOneFeatureInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/OneFeatureInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]
    FEATURES = ["ToLine"]

    @pytest.fixture
    def single(self):
        one_feature_inputs = email_mbmlbook.FeatureSet(
            self.XML, self.DATASETS, self.FEATURES
        )
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
