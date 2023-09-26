def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 != 0:
      return True
    elif year % 400 == 0:
      return True
  else:
    return False
year = int(input("Enter a year: "))
is_leap_year = is_leap_year(year)
if is_leap_year:
  print("The year {} is a leap year. That means it has 366 days instead of the usual 365.".format(year))
else:
  print("The year {} is not a leap year. That means it has 365 days.".format(year))