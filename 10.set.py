# Set
# 1. Create a set
# 1.1 create
my_set1 = {1, 2, 3, 4, 5}
# my_set2 = {1, 2, 2, 3, 3, 4, 4, 5, [1, 2]} # error because [1, 2]
print(f"my set 1: {my_set1}")
print(type(my_set1))

#1.2 length
print(f"length of my set 1: {len(my_set1)}")

my_set2 = {1, 2, 2, 3, 3, 4, 4, 5}
print(f"my set 2: {my_set2}")
print(f"length of my set 2: {len(my_set2)}")

# 2. Loop in set
my_set = {1, 2, 3, "a", 'b'}
for item in my_set:
    print(f'item: {item}')

# 3. Update set (add or remove)
my_set = {"a","b","c","d", "e"}
my_set.add('f')
my_set.add('a')
# my_set.remove('g') # error
my_set.remove('e')
my_set.discard("a")
my_set.discard("g") # no error
print(f"my set: {my_set}")

# 4. Work with sets
my_set10 = {1, 2, 3, 4, 5, 6, "b", "c", "d"}
my_set11 = {6, 7, 8, "a", "b", "c"}
# 4.1 intersection
new_intersection_set = my_set10.intersection(my_set11)
print(f"intersection: {new_intersection_set}")

# 4.2 union
new_union_set = my_set10.union(my_set11)
print(f"union: {new_union_set}")

# 4.2 symmetric difference = intersection - union
new_symmetric_difference_set1 = my_set10.symmetric_difference(my_set11)
print(f"symmetric_difference1: {new_symmetric_difference_set1}")

new_symmetric_difference_set2 = my_set11.symmetric_difference(my_set10)
print(f"symmetric_difference2: {new_symmetric_difference_set2}")