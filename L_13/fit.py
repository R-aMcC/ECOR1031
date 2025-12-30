# ECOR 1031 Lab 13 - fit module
# Remember to include type annotations for your functions

__author__ = "Ryan McCracken"
__student_number__ = "101375579"

import numpy as np
#==========================================#
# Place your curve_fit function after this line
def curve_fit(students: list[dict], attribute: str, degree: int) -> str:
    grade_to_attribute = {} 
    for student in students:
        grade = student["AvgGrade"]
        attribute_value = int(student[attribute])
        if attribute_value not in grade_to_attribute:
            grade_to_attribute[attribute_value] = []
        grade_to_attribute[attribute_value].append(int(grade))
    x_values = []
    y_values = []
    for attrib_value, grades in grade_to_attribute.items():
        avg_grade = sum(grades) / len(grades)
        i = 0
        while i < len(x_values) and x_values[i] < attrib_value:
            i += 1
        x_values.insert(i, attrib_value)
        y_values.insert(i, avg_grade)
    if degree > len(x_values) - 1:
        degree = len(x_values) - 1
    best_fit = np.polyfit(x_values, y_values, degree)

    return_str = "y = "
    for i in range(len(best_fit)):
        coeff = best_fit[i]
        if coeff != 0:
            if str(coeff).endswith(".0"):
                coeff = int(coeff)
            if coeff > 0 and i != 0:
                return_str += "+"
            elif coeff < 0:
                return_str += "-"
                coeff = abs(coeff)
            deg = len(best_fit) - i - 1
            if coeff == 1 and deg != 0:
                coeff = ""
            if deg == 0:
                return_str += f"{coeff}"
            elif deg == 1:
                return_str += f"{coeff}x"
            else:
                return_str += f"{coeff}x^{deg}"
    return return_str



# Do NOT include a main script in your submission
