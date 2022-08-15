# 1
# def hello():
#     print("Hello")

# hello()

# 2
# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     user_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {user_seconds}.")

# user_age_in_seconds()

# 3
friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends.append(friend_name)

add_friend()

print(friends)