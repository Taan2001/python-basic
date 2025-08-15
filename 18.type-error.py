# Some errors in Python
# SynTaxError
print("1. SynTaxError: \tOccurs when Python encounters invalid syntax")
# print "Hello World" # error
# if True
#    print "Hello World" # error

# NameError
print("2. NameError: \t\tUse a variable or function that hasn't been defined")
# print(helloWorld) # error

# IndexError
print("3. IndexError: \t\tOccurs when you try to access an index that is out of range for a list or other sequence type")
# my_list = [1, 2, 3, 4, 5]
# print(my_list[5]) # error
# print(my_list[-6]) # error
# print(my_list[-5]) # 1

#ModuleNotFoundError
print("4. ModuleNotFoundError: Occurs when Python can't find the module your're trying to import")
# import numpy1 as np #error
# my_array = np.array([1, 2, 3])
# print(my_array)

#AttributeError
print("5. AttributeError: \tOccurs when you try a access an attribute or method that doesn't exist on an object")
# my_str = "Hello World!"
# my_str.append("!")

# KeyError
print("6. KeyError: \t\tOccurs when trying to access a key in a dictionary that doesn't exist.")
# my_dict = {
#     "name": "Tan",
#     "age": 20
# }
# print(my_dict["address"]) # error

# TypeError
print("7. TypeError: \t\tOccurs when an operation or function is applied to an object of an inappropriate type")
# num = 10
# print(10 + 'abc') # error

# ImportError
print("8. ImportError: \tOccurs when Python cannot find the module being imported or there's an issue in the import statement")
# from numpy import abc # error

# ValueError
print("9. ValueError: \t\tOccurs when a function receives an argument of the right type but with an inappropriate value")
number = int("abc")
print(number)

# ZeroDivisionError
print("10. ZeroDivisionError: \tOccurs when a number is divided by zero")
# print(10 / 0) # error
