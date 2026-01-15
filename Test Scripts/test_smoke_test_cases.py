import pytest

class TestSmoke:

    @pytest.mark.smoke
    def test_smoke_test1(self):
        assert 1 == 1 ,"Both numbers are not equal"

    @pytest.mark.smoke
    def test_smoke_test2(self):
        assert 2 == 2 ,"Both numbers are not equal"

    @pytest.mark.smoke
    def test_smoke_test3(self):
        assert 3 == 3 ,"Both numbers are not equal"