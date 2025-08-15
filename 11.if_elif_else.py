# num = int(input("Enter a interger number: "))

# if num % 2 == 0:
#     print(f"The {num} is even number")
# else:
#     print(f"The {num} is odd number")

score = float(input("Enter your score: "))

if score > 8.5:
    print("You are excellent student")
elif score > 6.5:
    print("You are good student")
elif score > 5.:
    print("You are average student")
else:
    print("You are weak student")
