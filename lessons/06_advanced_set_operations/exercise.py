#1
my_list = [24, 36, 40]

#2
my_tuple = (5)

#3
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}

set2.add(77)
set2.add(9)
set2.add(12)

result = set1.intersection(set2) # {5, 77, 9, 12}
print(result)