# 1
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print("Even numbers is:")
for number in evens:
    print(number)


# 2
user_input = input("Enter your choice: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")