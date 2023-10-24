from die import Die

def test_die_roll():
    #Test rolling a 6-sided die
    die_6 = Die(6)
    result = die_6.roll()
    assert 1 <= result <= 6