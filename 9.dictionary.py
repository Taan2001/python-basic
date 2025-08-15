### Dictionary - {"key": value}
#1. Create dictionary
name_age = {
    "John": 5,
    "Senna": 10,
    "Lucia": 20
}

print(name_age)
print(type(name_age))
print(len(name_age)) # 3 key - value

#2. Get value of key
print(name_age["John"])
print(name_age["Senna"])
print(name_age["Lucia"])

#3. Change value of key
name_age["John"] = 1.5
name_age["Senna"] = 2.5
print(name_age)

#4. Loop in dictionary
#4.1 loop with keys
# for k in name_age.keys():
for k in name_age:
    print(k)

#4.2 loop with values
for k in name_age.values():
    print(k)

#4.3 loop both keys and values   
for k, v in name_age.items():
    print(f"{k}: {v}") 