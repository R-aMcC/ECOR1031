# ECOR 1031 Lab 12 - sort module
# Remember to include type annotations for your functions

__author__ = "Ryan McCracken"
__student_number__ = "101375597"


#==========================================#
# Place your sort_students_age_bubble function after this line
def sort_students_age_bubble(students: list[dict], order: str) -> str:
    if len(students) == 0:
        return "Empty list."
    swapped = True
    for student in students:
        if "Age" not in student:
            return "List not sorted. Age key not present."
    while swapped:
        swapped = False
        for i in range(len(students)- 1):
            if (students[i]['Age'] > students[i + 1]['Age'] and order == 'A') or (students[i]['Age'] < students[i + 1]['Age'] and order == 'D'):
                students[i], students[i + 1] = students[i + 1], students[i]
                swapped = True
    return "List sorted."
#==========================================#
# Place your sort_students_time_selection function after this line
def sort_students_time_selection(students: list[dict], order: str) -> str:
    if len(students) == 0:
        return "Empty list."
    for student in students:
        if "StudyTime" not in student:
            return "List not sorted. StudyTime key not present."
    for min_index in range(len(students)-1):
        index = min_index
        for i in range(min_index+1, len(students)):
            if (students[i]['StudyTime'] < students[index]['StudyTime'] and order == 'A') or (students[i]['StudyTime'] > students[index]['StudyTime'] and order == 'D'):
                index = i
        if min_index != index:
            students[min_index], students[index] = students[index], students[min_index]
    return "List sorted."

#==========================================#
# Place your sort_students_avg_insertion function after this line
def sort_students_avg_insertion(students: list[dict], order: str) -> str:
    if len(students) == 0:
        return "Empty list."
    for student in students:
        if "AvgGrade" not in student:
            return "List not sorted. AvgGrade key not present."
    for i in range(1, len(students)):
        key_student = students[i]
        j = i - 1
        while j >= 0 and ((students[j]['AvgGrade'] > key_student['AvgGrade'] and order == 'A') or (students[j]['AvgGrade'] < key_student['AvgGrade'] and order == 'D')):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student
    return "List sorted."

#==========================================#
# Place your sort function after this line
def sort(students: list[dict], order: str, key: str) -> str:
    if key == "Age":
        return sort_students_age_bubble(students, order)
    elif key == "StudyTime":
        return sort_students_time_selection(students, order)
    elif key == "AvgGrade":
        return sort_students_avg_insertion(students, order)
    else:
        return f"Invalid input, the list cannot be sorted by {key}."

# Do NOT include a main script in your submission
