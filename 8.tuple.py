### Tuple
# 1. Create tuple
tuple_1 = ("a", 2)
print(tuple_1)
print(type(tuple_1))

tuple_1 = ("a") # type => string
tuple_1 = ("a",) # type => tuple
print(tuple_1)
print(type(tuple_1))


# 2. Loop in Tuple
tuple_1 = ('a', 'b', [1, 2], 3, 4.5)
print(f"length of Tuple: {len(tuple_1)}")
for item in tuple_1:
    print(item)

# 3. Index
# index: 0 => len(tuple) - 1
print(tuple_1[0])

# index: -len(tuple) => - 1
print(tuple_1[-1])

# 4. Addition Tuples
# 4.1
tuple_1 = ("a", "b")
tuple_2 = (1, 2, True)

new_tuple = tuple_1 + tuple_2
print(f"New tuple: {new_tuple}")

# 4.2
tuple_1 = ('a', 'b', [1, 2], 3, 4.5)
list_1 = list(tuple_1)
list_1.append("hello")
new_tuple = tuple(list_1)
print(f"New Tuple: {new_tuple}")

# 5. Remove a element
# 5.1 
tuple_1 = ('a', 'b', [1, 2], 3, 4.5)
list_1 = list(tuple_1)
# list_1.remove(5) # error because 5 is not exist
list_1.remove(4.5)
new_tuple = tuple(list_1)
print(f"New Tuple: {new_tuple}")


# 6. Count 
tuple_1 = ('a', 'b', ['a', 2], 'a', 3, 4, 5, 4.5, 'a')
print(tuple_1.count('a')) # 3
print(tuple_1.count(['a', 2])) # 1
print(tuple_1.count(['a', 2, 3])) # 0

# 7. Immutable
tuple_3 = ('a', 'b', 'a', 3, 4, 5, 4.5, 'a')
tuple_4 = ('a', 'b', 'a', 3, 4, 5, 4.5, 'a')

print(f"ID of tuple_3: {id(tuple_3)}")
print(f"ID of tuple_4: {id(tuple_4)}")

tuple_5 = ('a', 'b', [2], 'a', 3, 4, 5, 4.5, 'a')
tuple_6 = ('a', 'b', [2], 'a', 3, 4, 5, 4.5, 'a')

print(f"ID of tuple_5: {id(tuple_5)}")
print(f"ID of tuple_6: {id(tuple_6)}")

# tuple_5[0] = 2 # error
# tuple_5[2] = [3] # error
tuple_5[2][0] = 1 
print(tuple_5)


