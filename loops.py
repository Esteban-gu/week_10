# While loop = execute some code WHILE some condition remains true

# Example 1

# name = input("Enter your name:")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# Example 2

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# Example 3

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("Bye bye")

# Example 4

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# print(f"Your number is {num}")


# for loops = execute a block of code a fixed number of times.
#                   You can iterate over a range, string, sequence, etc.

# Example 1

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

# Example 2

# for x in range(1, 21):
#     if x == 13:
#         continue    # This skips a number
#     else:
#         print(x)

# Example 3

# for x in range(1, 21):
#     if x == 13:
#         break    # This stops at a certain number
#     else:
#         print(x)

# Challenge 1

list_of_names = ['John', 'Paul', 'George', 'Ringo']

for name in list_of_names:
    if name == 'George':
        print('George was found!')
    else:
        print('George was not found!')
        print(name)

# Challenge 2

list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']

for name in list_of_names2:
    if name == 'Ironman':
        continue
    print(name)

# Challenge 3
    
list_of_names3 = ['Thanos', 'Ironman', 'Thor', 'Hulk']

for name in list_of_names3:
    if name == 'Thanos':
        name = 'Spiderman'
    print(name)