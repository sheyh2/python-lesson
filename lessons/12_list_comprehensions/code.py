# 1
# numbers = [1, 3, 5]
# doubled = [x * 2 for x in numbers]

# 2
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print(friends is starts_s) # print(friends[0] is starts_s[0]) it is true
print("frinds: ", id(friends), "starts_s:", id(starts_s))