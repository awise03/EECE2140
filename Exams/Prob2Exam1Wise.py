def process_students(student_list):
    updated_student_list = {}
    for name, (date, grades) in student_list.items():
        gpa = sum(grades) / len(grades)
        if date in updated_student_list:
            updated_student_list[date].append((name, round(gpa, 2)))
        else:
            updated_student_list[date] = [(name, gpa)]
    return updated_student_list

student_list = {'Alice':(2023, [3.5, 2.9, 3.1, 3.8]), 'Bob':(2024, [3.0, 2.6]), 'Morgan':(2024, [2.8, 3.9, 3.7]), 'Tim':(2023, [2.5])}
print(process_students(student_list))