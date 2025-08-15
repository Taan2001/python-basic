import re 

# re.match: 
# 1.
my_string = "Hello World! My name is Taan"
match1 = re.match("Hello", my_string)

print(match1)
print(match1.span())
print(match1.group())

# 2.
my_string = "Hello World! My name is Taan"
match1 = re.match('World', my_string)

print(match1)
# print(match1.span()) # error
# print(match1.group()) # error


# re.search: 
# 1.
my_string = "Hello World! My name is Taan"
# search1 = re.search("World", my_string)
search1 = re.search("e", my_string)

print(search1)
print(search1.span())
print(search1.group())

# re.findall: 
# 1.
my_string = "Hello World! My name is Taan"
# findall1 = re.findall("World", my_string)
findall1 = re.findall("e", my_string)

print(findall1)
print(type(findall1))


# re.split: 
# 1.
my_string = "Hello World! My name is World"
split1 = re.split("World", my_string)
# split1 = re.split(" ", my_string)

print(split1)
print(type(split1))

# re.sub: 
# 1.
my_string = "Hello World! My name is World"
# sub1 = re.sub("World", my_string)
sub1 = re.sub("World", "Taan", my_string)

print(sub1)
print(type(sub1))