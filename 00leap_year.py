c_year = int(input("Enter the current year: "))
e_year = int(input("Enter the year up to which you want to find leap years: "))
print("Leap years between", c_year, "and", e_year, "are:")
for year in range(c_year, e_year + 1):
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		print(year)
