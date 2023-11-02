import pytest

from addOnePT import add_one

class TestAddOne:
    def test_add_one(self):
        assert add_one(3) == 4

    @pytest.mark.xfail
    def test_add_one_failed(self):
        assert add_one(3) == 3
