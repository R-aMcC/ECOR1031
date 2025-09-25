# ECOR 1031 Lab 4

__author__ = "Ryan McCracken"
__student_number__ = "101375597"

import math

# ====================================================
# Exercise 1

def area_of_disk(radius):
# Type your function definition for Exercise 1 here.
    return math.pi * radius ** 2
# =======================================================
# Exercise 2
LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
# Type your function definition for Exercise 2 here.
    return 100 * LITRES_PER_GALLON / mpg / KMS_PER_MILE
# =======================================================
# Exercise 3

def accumulated_amount(principal, rate, n, time):
# Type your function definition for Exercise 3 here.
    return principal * (1 + rate / n) ** (n * time)
# =======================================================
# Exercise 4

def lateral_area_of_cone(height, radius):
# Type your function definition for Exercise 4 here.
    return math.pi * radius * math.sqrt(height ** 2 + radius ** 2)
# =======================================================
# Exercise 5
def coupon(grocery_bill):
# Type your function definitions for Exercise 5 here.

    if grocery_bill < 10:
        return 0
    elif grocery_bill <= 60:
        return grocery_bill*0.08
    elif grocery_bill <= 150:
        return grocery_bill*0.1
    elif grocery_bill <= 210:
        return grocery_bill*0.12
    else:
        return grocery_bill*0.14
    
# =======================================================
# Exercise 6
def bakers_party(weekend, pastries):
# Type your function definitions for Exercise 6 here.
    return weekend and pastries >= 40 or 40 <= pastries <= 60
# =======================================================
# Exercise 7
def squirrel_play(summer, temperature_f):
# Type your function definitions for Exercise 7 here.
    return 60 <= temperature_f <= (100 if summer else 90)
# =======================================================
# Exercise 8
def great_42(num1, num2):
# Type your function definitions for Exercise 8 here.
    return num1 == 42 or num2 == 42 or num1 + num2 == 42 or abs(num1 - num2) == 42
