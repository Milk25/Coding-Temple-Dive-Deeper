year = float(input("What is the year: "))

# if year % 100 == 0:
#     print("Is not a leap year: ")
# elif (year % 4 == 0 and year % 400 == 0):
#     print("It is a leap year: ")


if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Is a leap year: ")
else:
    print("Not a leap year: ")