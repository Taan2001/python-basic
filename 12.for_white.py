"""
    Loop in python
"""

my_list = [1, 2, 3, 4, 5, 6, 7]
# for
# for item in my_list: 
#     print(item)

# for i in range(len(my_list)):
#     print(f"index {i}: {my_list[i]}" )

# # while
# count = 0
# while count < 5: 
#     print(f"hello world - {count}")
#     count+=1

# # break, continue
# for item in my_list:
#     if(item < 3): 
#         continue
#     else:
#         if (item == 6): 
#             break
#         print(f"item: {item}")

count = 0
while count < 10: 
    if count % 2 == 0:
        
        count+=1
        continue
    else:
        if count == 7: 
            break
        print(f"count: {count}")
        count+=1
    