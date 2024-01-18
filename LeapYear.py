def isPositive (year):
    if year > 0:
        a = isDivisibleby4(year)
        return a
    else:
        return 0
def isDivisibleby4(year):
    if year % 4 == 0:
        a = CheckForCenturyYear(year)
        return a
    else:
        return 0
def CheckForCenturyYear(year):
    if year % 100 != 0 or year % 400 == 0:
        return 1
    else:
        return 0
y = int(input("Enter a year:"))
if isPositive(y):
    print("Given Year is a Leap Year")
else:
    print("Given Year is not a Leap Year")
