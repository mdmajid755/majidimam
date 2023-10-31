import pytest
import addOnePT

class TestaddOne :
    def test_addOne(self):
        assert addOnePT.addOne(3) == 4

    @pytest.mark.xfail
    def test_addOneFailure(self):
        assert addOnePT.addOne(3) == 5