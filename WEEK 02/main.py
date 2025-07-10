
# * If condition

birth_year = int(input("Please enter your date of birth: "))

current_year = 2025

age = current_year - birth_year

if age >= 13:
    print("You can proceed to watch the movie")
else:
    print("You have not met the requirement for minimum required age for this movie")
