"""
    open(file_Name, mode)
    mode: 
        + r - Read: default value - error if the file does not exist
        + a - Append: create the if it does not exist
        + w - Write: create the file if it does not exist
        + x - Create: return an error if the file exists
"""

"""
    Read file "rt"
"""

# 1. 
file_obj = open("source_dir/abc.txt", 'rt')
content = file_obj.read()
print(f"file: {file_obj}")
print(f"content: {content}")
file_obj.close()

# 2.
with open("source_dir/hello-world.txt", 'rt') as file_obj: 
    content = file_obj.read()
    print(f"content: {content}")

"""
    Write file "w"
"""
with open("source_dir/new.txt", 'w') as file_obj: 
    content = file_obj.write("I'm learning Python")

"""
    Continue writing file "a"
"""
with open("source_dir/new-file.txt", 'a') as file_obj: 
    content = file_obj.write("\nI will do it")

"""
    Create file "x"
"""
with open("source_dir/new-file1.txt", 'x') as file_obj: 
    pass



