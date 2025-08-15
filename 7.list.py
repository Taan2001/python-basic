# create a list
my_list = [1, 1.2, 'string', True, [2, 3]]
print(my_list)
print(type(my_list))

# create a empty list
empty_list1 = []
print(empty_list1)
print(type(empty_list1))
# empty_list2 = list()
# print(empty_list2)
# print(type(empty_list2))

# length of list
print(len(my_list))

# index
# index: 1 => len(list) - 1
print(my_list[0])
print(my_list[4])
# index: -len(list) => - 1
print(my_list[-5])
print(my_list[-1])

# Slicing
print(my_list[0:5]) # get elememt: 0, 1, 2, 3, 4
print(my_list[2:]) # get elememt: 2, 3, ..., len(list) - 1
print(my_list[-5:-2]) # get element: -5, -4, -3  
print(my_list[-4:]) # get element: -4, -3, ..., -1  

# loop in list
for x in my_list:
    print(x)

# concat list
list1 = [1, 4.6, 2]
list2 = ["anh", "em", True]
concat_lst1 = list1 + list2
print(concat_lst1)

#immutable in Python
lst = [1, 2, 3, True]
lst[3] = 4
print(lst)


# Methods
# 1. add list element (1 element) in the last of the list .append()
my_lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
my_lst1.append(50)
print(my_lst1)

# 2. add elements .extend()
my_lst2 = ["anh", "em"]
my_lst1.extend(my_lst2)
print(my_lst1)

# 3. sort list .sort() or sorted()
my_lst1 = [1, -2, -3, -4, 10, -5, -6, -7, -8]
my_lst1.sort()
print(my_lst1)
my_lst1.sort(reverse=True)
print(my_lst1)

my_lst1 = [1, -2, -3, -4, 10, -5, -6, -7, -8]
new_lst = sorted(my_lst1)
print(my_lst1)
print(new_lst)

# 4. reverse list
my_lst1 = [1, -2, -3, -4, 10, -5, -6, -7, -8]
new_lst = my_lst1[::-1] # start:stop:step
my_lst1.reverse()
print(my_lst1)
print(new_lst)

# 5. insert element .insert(index, value)
my_lst1 = [1, 2, 3]
my_lst1.insert(0, [True, False])
print(my_lst1)
my_lst1.insert(100, ['a', 'b'])
print(my_lst1)

# 6. delete element del or .remove(ele)
my_lst1 = [1, 2, 3.5, 'anh', True]
del my_lst1[0] # index: -len(list) => len(list) - 1
print(my_lst1)

my_lst1 = [1, 2, 3.5, 'anh', True]
del my_lst1[-1] # index: -len(list) => len(list) - 1
print(my_lst1)

my_lst1 = [1, 2, 3.5, 'anh', True]
del my_lst1[:-1] # index: -len(list) => len(list) - 1
print(my_lst1)


# 7. return the first index of the element == value .index() - if not exist => error
my_lst1 = [1, 2, 3.5, 'anh', True]
index = my_lst1.index(2)
print(index)
# print(my_list.index(100)) # error

# 6. get and remove element of the list .pop(index)   
my_lst1 = [1, 2, 3.5, 'anh', True]
ele = my_lst1.pop(3)
print(ele)
print(my_lst1)
