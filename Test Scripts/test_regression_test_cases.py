import pytest

class TestRegression:
    @pytest.mark.regression
    def test_regression_test1(self):
        assert 1 == 1 ,"Both numbers are not equal"

    @pytest.mark.regression
    def test_regression_test2(self):
        assert 1 == 2 ,"Both numbers are not equal"

    @pytest.mark.regression
    def test_regression_test3(self):
        assert 1 == 3 ,"Both numbers are not equal"