# print("Hello World")

# name = "Ayana"
# year = 2018
#
# if year > 2020:
#     print("year is greater than 2020")
# elif year >= 1990:
#     print("1990 <= year < 2020")
# else:
#     print("less than 1990")

# PEP 8
# score  = input("Please enter your score: ") # prompt message
# score = int(score) # int(), float(), str()
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")
#
# print(score)

# Definition of function
# something goes in (sometime with parameter) and go through some instructions and something goes out.

# - range(start, end)
# ex) range(1, 10) - 1, 2, 3, ..., 9
# - range(start=0, end, steps=1)
# ex) range(1, 10, 2) - 1, 3, 5, 7, 9

# total = 0
# for i in range(1, 11):
#     total = total + i
#     print(total)

# Factorial
result = 1
n = int(input("Please enter integer: "))

for i in range(n, 0, -1):
    result = result * i
print(result)






