# 1
# friend_ages = {
#     "Rolf": 24,
#     "Adam": 30,
#     "Anne": 27
# }

# friend_ages["Rolf"] = 20

# print(friend_ages)

# 2
# friends = [
#     {
#         "name": "Rolf",
#         "age": 24
#     },
#     {
#         "name": "Adam",
#         "age": 30
#     },
#     {
#         "name": "Anne",
#         "age": 27
#     },
# ]

# print(friends)

# 3
student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100
}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# 4

# student_attendance = {
#     "Rolf": 96,
#     "Bob": 80,
#     "Anne": 100
# }

# attendance_values = student_attendance.values()
# print(sum(attendance_values) / len(attendance_values))