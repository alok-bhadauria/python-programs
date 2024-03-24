def leapyear(year):
    return("Leap year" if ((year%4==0 and year%100!=0) or year%400==0) else "Not a leap year")
year = int(input("Enter the year : "))
out = leapyear(year)
print(out)