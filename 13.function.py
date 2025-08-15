"""
    Function in Python
"""

def sum(x, y):
    return x + y

def print_value(value):
    print(f"The value is: {value}")

a = 2
b = 20
print_value(sum(a,b))

import shutil
import os 


source_dir = "source_dir"
# des_dir = "des_dir"
# list_name = os.listdir(source_dir) # return string[]

# print(list_name)

# for file_name in list_name:
#     shutil.copy(os.path.join(source_dir, file_name), os.path.join(des_dir, file_name))

def copy_clone(source_dir, des_dir):
    list_name = os.listdir(source_dir) # return string[]
    
    for file_name in list_name:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(des_dir, file_name))



source_dir = "source_dir"
des_dir = "des_dir"

copy_clone(source_dir, des_dir)