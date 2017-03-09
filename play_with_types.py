# case 1: string
variable = "Hello, world!"
print(type(variable))  # it should be "str"
print(variable)

# case 2: integer number
variable = 1234
print(type(variable))  # it should be "int"
print(variable)

# case 3: floating point number
variable = 1.23
print(type(variable))  # it should be "float"
print(variable)

# case 4: another number (sort of)
variable = 0o1234
print(type(variable))  # it should be "int"
print(variable)
