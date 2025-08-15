# """
#     Higher Order functions
# """

# # 1. Take one or more functions as arguments
# def cal_sum(nums):
#     return sum(nums)

# def higher_order_func(my_func, my_list):
#     my_sum = my_func(my_list)
#     return my_sum

# my_result = higher_order_func(cal_sum, [1, 2, 3, 4, 5])
# print(f"My result: {my_result}")

# # 2. Return a function as its result
# def cal_min(a, b):
#     if a < b: 
#         return a
#     return b 

# def cal_max(a, b):
#     if a < b: 
#         return b
#     return a

# def higher_order_func2(cal_name):
#     if cal_name == 'min':
#         return cal_min
#     return cal_max

# my_result1 = higher_order_func2("min")
# my_result2 = higher_order_func2("max")

# print(f"My result1: {my_result1(10, 20)}")
# print(f"My result2: {my_result2(20, 3.2146)}")


# """
#     Decorators
# """
# # 1. No argument => use the higher-order function
# def decorator_example(func):
#     def wrapper():
#         print("Before the function is called")
#         func()
#         print("After the function is called")

#     return wrapper

# def wrapped():
#     print("hello world")

# my_func = decorator_example(wrapped)
# my_func()

# # 2. Use decorator
# def decorator(func):
#     def wrapper():
#         print("Before the decorator function is called")
#         func()
#         print("After the decorator function is called")
#     return wrapper

# @decorator
# def say_hello():
#     print("hello world")

# say_hello() # = decorator(say_hello) - call directly from wrapped function

# Practice
def decorator_func(func):
    def wrapper(name, age):
        print("Good morning!")
        func(name, age)
        print("Nice to meet you!!!")
    return wrapper

@decorator_func
def say_hello(name, age):
    print(f"Hi, my name's {name}, I'm {age} years old")

say_hello("An", 25)
