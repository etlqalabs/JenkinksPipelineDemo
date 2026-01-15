import pytest

class TestComponent:

    @pytest.mark.component
    def test_component_test1(self):
        assert 1 == 1 ,"Both numbers are not equal"

    @pytest.mark.component
    def test_component_test2(self):
        assert 2 == 2 ,"Both numbers are not equal"

    @pytest.mark.component
    def test_component_test3(self):
        assert 3 == 3 ,"Both numbers are not equal"