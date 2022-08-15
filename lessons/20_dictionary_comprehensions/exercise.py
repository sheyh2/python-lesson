# 1
student = {
    "name": "Jose",
    "school": "Computing",
    "grades": (66, 77, 88)
}

# 2
def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)

# 3
def average_grade_all_students(student_list): 
    total = 0
    count = 0

    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])
    
    return total / count

print(average_grade_all_students(student))