# Conversion Calculator
# By: Brianna Babcock

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number to convert? "))
user_unit = input("What unit is your number?")

# to convert in to mm --> in x 25.4
# to convert mm to in --> mm / 25.4

# user gives in unit
conv_number = user_number * 25.4

print(conv_number)
print(user_unit)

