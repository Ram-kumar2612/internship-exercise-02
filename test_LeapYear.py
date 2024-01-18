import LeapYear

def test_isPositive():
    assert LeapYear.isPositive(5) == 1
    assert LeapYear.isPositive(0) == 0
    assert LeapYear.isPositive(-5) == 0
def test_isDivisibleby4():
    assert LeapYear.isDivisibleby4(100) == 1
    assert LeapYear.isDivisibleby4(123) == 0
def test_CheckForCenturyYear():
    assert LeapYear.CheckForCenturyYear(800) == 1
    assert LeapYear.CheckForCenturyYear(300) == 0
