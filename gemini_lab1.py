import random
def average_grade(grades):
    average = sum(grades)/len(grades)
    return int(average)

students = [
    {
        'name': 'Alice',
        'id': 101,
        'courses': {
            'Math': random.randint(0,100),
            'Politics': random.randint(0,100),
            'Physics': random.randint(0,100),
            'Art': random.randint(0,100),
            'History': random.randint(0,100)
        }
    },
    {
        'name': 'Brian',
        'id': 102,
        'courses': {
            'Math': random.randint(0,100),
            'Physics': random.randint(0,100),
            'Chemistry': random.randint(0,100),
            'History': random.randint(0,100)
        }
    },
    {
        'name': 'Charlie',
        'id': 103,
        'courses': {
            'Math': random.randint(0,100),
            'History': random.randint(0,100)
        }
    },
    {
        'name': 'Ian',
        'id': 104,
        'courses': {
            'Math': random.randint(0,100),
            'Physics': random.randint(0,100),
            'Biology': random.randint(0,100),
            'History': random.randint(0,100)
        }
    },
    {
        'name': 'Kirk',
        'id': 105,
        'courses': {
            'Math': random.randint(0,100),
            'Physics': random.randint(0,100),
            'Science': random.randint(0,100)
        }
    },
]
'''
for student in students:
    student_name = student["name"]
    print(f"Report card for {student['name']}:")
    for course in student["courses"]:
        print(f"A {student['courses'][course]} in {course}")
    print()


for student in students:
    grades = []
    student_name = student["name"]
    for course in student["courses"]:
        grades.append((student["courses"][course]))
    print (f"{student_name} has a: {average_grade(grades)} average grade.")
'''
# Identify students who need help. 
# Using a comprehension with a conditional, 
# create a new list containing the names of 
# all students whose average grade is below 75. 
# Print this list.
# [expression for item in iterable if condition]

best_mather_grade = 0
best_mather = ""
worst_mather_grade = 0
worst_mater = ""