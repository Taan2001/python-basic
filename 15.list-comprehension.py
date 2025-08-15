"""
    List Comprehension
"""

# Create
# 1. normal
lst = [1, 2, 3, 4, 5]
new_lst = []

for x in lst:
    new_lst.append(x ** 2)

print(f"new lst: {new_lst}")

# 2. use list comprehension
# [Expression for item in iterable] 
new_lst2 = [x ** 3 for x in lst] 
print(f"new lst2: {new_lst2}")

# filter
lst = [1, 2, 3, 4, 5]
# [Expression for item in iterable if condition == True] 
new_lst3 = [x for x in lst if x % 2 == 0 ]
print(f"new lst3: {new_lst3}")

# [Expression1 if condition == True else Expression1 for item in iterable] 
new_lst4 = [x  if x % 2 == 0 else "x" for x in lst]
print(f"new lst4: {new_lst4}")

"""
    Dictionary Comprehension
"""
lst = [1, 2, 3, 4, 5]
# {keys: value for item in iterable} 
new_dict1 = {k: k**2 for k in lst}
print(f'new dict1: {new_dict1}')

"""
    Set Comprehension
"""
my_string = "ngoctaan"
# {item for item in iterable} 
new_set1 = {letter for letter in my_string}
print(f'new set1: {new_set1}')

lst = [1, 1, 2, 1, 3, 3, 4, 5]
# {item for item in iterable} 
new_set2 = {item for item in lst}
print(f'new set2: {new_set2}')

"""
    Multiple Loops
"""
nested_lst = [[i+1 for i in range(5)] for _ in range(10)]
print(f"nested list: {nested_lst}")


arr_2d = [
    [1, 2, 3], 
    [4, 5, 6],  
    [7, 8, 9]
]

flatten_lst = [num for row in arr_2d for num in row] # don't recommend
print(f"flatten lst: {flatten_lst}")

new_lst = []
for row in arr_2d:
    for num in row:
        new_lst.append(num)

print(f"new lst: {new_lst}")
