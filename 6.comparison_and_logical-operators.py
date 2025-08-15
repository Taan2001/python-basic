### comparison operators
# equal
print("# equal:")
print(20 == 20) # True
print(20 == '20') # False
print("anh" == 'em') # False

# not equal
print("\n# not equal:")
print(20 != 20) # False
print(20 != '20') # True
print("anh" != 'em') # True

# >, >=, < , <=
print('\n# >, >=, < , <= :')
print(10 > 10) # False
print(10 >= 10) # True
print(10 < 10) # False 
print(10 <= 10) # True
# print(10 <= '10') # Error

# logical operators
print('\n# logical operators:')
# and:
num1 = 15
print("Number1 is in the range [10, 20]:", num1 >= 10 and num1 <= 20)
print("Number1 is in the range [10, 20]:", 10 <= num1 <= 20)

# or:
num2 = 21
print("Number2 is in the range [10, 20]:", num2 >= 10 and num2 <= 20)
print("Number2 is out of the range [10, 20]:", 10 > num2 or 20 < num2)

# not:
is_boolean = True
print(not is_boolean)
print(not 5 > 5)