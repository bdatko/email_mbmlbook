import email_mbmlbook
import pandas as pd
import pytest


class TestSeperateInputs:

    XML = "https://raw.githubusercontent.com/dotnet/mbmlbook/main/src/4.%20Uncluttering%20Your%20Inbox/Data/SeparateInputs.objml"
    DATASETS = ["Train", "Validation", "Test"]
    SOURCE = "data/SeparateInputs_objml.csv"

    @pytest.fixture
    def seperate(self):
        return pd.read_csv(self.SOURCE)

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
