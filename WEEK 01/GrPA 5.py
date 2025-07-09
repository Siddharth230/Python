# int: Read a number as integer from standard input
age = int(input())

# str: Read a string of format dd/mm/yy from standard input
dob = input()

# int, int, int: Get the correct parts from dob as int
day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:])

# str: fifth birthday formatted as day/month/year
fifth_birthday = str(day) + "/" + str(month) + str(year+5)

# str: last birthday formatted as day/month/year
last_birthday = str(day) + "/" + str(month) + str(year-1)

# str: dob same day after 10 months formatted as day/month/year
month += 10
month, year = (month - 1) % 12 + 1, year + (month - 1) // 12
tenth_month = str(day) + "/" + str(month) + str(year)

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(tenth_month, fifth_birthday, last_birthday, sep=",")

# float: Read a number as float from stdin(Standard input)
weight = float(input)

# str: reformat weight of format 55 kg 250 grams
kg = int(weight)
grams = int((weight - kg) * 1000)
weight_readable = str(kg) + " kg " + str(grams) + " grams"

# print weight_readable
print(weight_readable)
