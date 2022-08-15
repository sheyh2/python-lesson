# 1
# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0.")
    
#     return dividend / divisor

# def calculate(*values, operator):
#     return operator(*values)

# result = calculate(20, 0, operator=divide)
# print(result)

# 2
from operator import itemgetter


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

# replace lambde
# def get_friend_name(friend):
#     return friend["name"]

print(search(friends, "Rolf Smith", itemgetter("name"))) # lambda friend: friend["name"]