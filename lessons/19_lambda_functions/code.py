# 1
# add = lambda x, y: x + y

# print(add(5, 7))

# 2
def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
# doubled = [double(x) * 2 for x in sequence]
# doubled = list(map(lambda x: x * 2, sequence))
doubled = list(map(double, sequence))
print(doubled)