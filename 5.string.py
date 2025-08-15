my_string = "hello world!"
print(my_string)
print(type(my_string))

# length of the string
print(len(my_string))

# index
# index: 0 => len(string) - 1
print(my_string[10])
# print(my_string[100]) # error

# index: -len(string) => - 1
print(my_string[-12])
# print(my_string[-13]) # error

# Slicing for string
print(my_string[1:4]) # get indices: 1, 2, 3
print(my_string[1:]) # get indices: 1, 2, 3, ..., len(string) - 1 
print(my_string[-12:-8]) # get indices: -12, -11, -10, -9
print(my_string[-12:]) # get indices: -12, -11, -10, -9, ..., -1

# loop in for string.
for str in my_string:
    print(str)

# check string in string

if "hello" in my_string:
    print("Ok")
else:
    print("No")

# Methods
print(my_string.upper())
print(my_string.lower())

# string in immutable in Python
my_str = "hello world!"
# my_str[0] = "H" # error
# my_str[6] = "W" # error 
my_str = "Hello World!"
print(my_str)
