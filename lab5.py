# ECOR 1031 Lab 5

__author__ = "Ryan McCracken"
__student_number__ = "101375597"

import math

# ======================================================
# Exercise 1
def tip(bill: float, satisfaction: int) -> float:
    """Return the tip amount based on bill and satisfaction.

    Preconditions: bill >= 0, satisfaction in {1, 2, 3}

    >>> tip(100, 1)
    20.0
    >>> tip(50, 2)
    7.5
    >>> tip(30, 3)
    3.0
    """
    if satisfaction == 1:
        return bill * 0.2
    elif satisfaction == 2:
        return bill * 0.15
    else:
        return bill * 0.05
# Type your function definition for Exercise 1 here.
# ======================================================
# Exercise 2
def multiply_uniques(a: int, b: int, c: int) -> int:
    """Return the product of all unique numbers between the three input parameters and 1 if all are equal.

    Preconditions: N/A

    >>> multiply_uniques(1, 2, 3)
    6
    >>> multiply_uniques(3, 3, 3)
    1
    >>> multiply_uniques(3, 3, 2)
    2

    """
    if a == b == c:
        return 1
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a * b * c
# Type your function definition for Exercise 2 here.

# ======================================================
# Exercise 3
def area_of_disk(radius: float) -> float:
    """Return the area of a disk with the given radius.

    Preconditions: radius >= 0

    >>> area_of_disk(1.0)
    3.141592653589...
    >>> area_of_disk(0)
    0.0
    >>> area_of_disk(2.0)
    12.566370614359...
    """
    return math.pi * radius ** 2

def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Return the distance between two coordinates.

    Preconditions: N/A

    >>> distance(0, 0, 3, 4)
    5.0
    >>> distance(0, 0, 0, 0)
    0.0
    >>> distance(8, 7, 1, 3)
    7.615773105863909 
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_of_circle(x1: int, y1: int, x2: int, y2: int) -> float:
    """
    Return the area of a circle given the coordinates of its center and a point on its circumference.

    Preconditions: N/A

    >>> area_of_circle(0, 0, 0, 0)
    0.0
    >>> area_of_circle(0, 0, 3, 4)
    78.53981633974483
    >>> area_of_circle(-1, -1, 2, 3)
    28.274333882308138
    """
    return area_of_disk(distance(x1, y1, x2, y2))
# Type your function definition for Exercise 3 here.

# ======================================================
# Exercise 4
def parrot_trouble(talking: bool, hour: int) -> bool:
    """
    Return True if the parrot is talking before 7:00 (7 AM) or after 20:00 (8 PM) 

    Preconditions: 0 <= hour <= 23

    >>> parrot_trouble(True, 6)
    True
    >>> parrot_trouble(True, 7)
    False
    >>> parrot_trouble(False, 22)
    False
    """
    return talking and (hour < 7 or hour > 20)
# Type your function definition for Exercise 4 here.

# ======================================================
# Exercise 5
def alarm_clock(day: int, vacation: bool) -> str:
    """
    Return the time the alarm clock should ring based on the day and if it's a vacation.

    Preconditions: 0 <= day <= 6

    >>> alarm_clock(1, False)
    "7:00"
    >>> alarm_clock(6, True)
    "off"
    >>> alarm_clock(0, False)
    "10:00"
    """
    if vacation and day % 6 == 0:
        return "off"
    elif vacation or day % 6 == 0:
        return "10:00"
    else:
        return "7:00"
# Type your function definition for Exercise 5 here.

# ======================================================
# Exercise 6
def close_far(a: int, b: int, c: int) -> bool:
    """
    Return True if one of b or c is within 1 of a while the other is at least 2 away from both other numbers

    Preconditions: N/A

    >>> close_far(1, 2, 10)
    True
    >>> close_far(1, 2, 3)
    False
    >>> close_far(4, 1, 3)
    True
    """
    return abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2 or abs(a - c) <= 1 and abs(a - b) >= 2 and abs(b - c) >= 2
# Type your function definition for Exercise 5 here.

# ======================================================
# Exercise 7
def blackjack(a:int, b:int) -> int:
    """Return the highest value 21 or under from the given inputs, returning 0 if both are over 21.

    Preconditions: a >= 0, b >= 0

    >>> blackjack(19, 22)
    19
    >>> blackjack(21, 10)
    21
    >>> blackjack(22, 22)
    0
    """
    if a > 21 and b > 21:
        return 0
    if a > 21 or b > 21:
        return min(a, b)
    return max(a, b)

# Type your function definition for Exercise 5 here.

# ======================================================
# Exercise 8
def assistance(income:float, children:int) -> float:
    """Return the amount of assistance based on income and number of children.

    Preconditions: income >= 0, children >= 0

    >>> assistance(15000, 1)
    2000.0
    >>> assistance(50000, 4)
    0.0
    >>> assistance(25000, 3)
    3000.0
    """
    if income < 20000:
        return 2000 * children
    elif income < 30000 and children >= 2:
        return 1000 * children
    elif 30000 <= income < 40000 and children >= 3:
        return 1500 * children
    return 0
# Type your function definition for Exercise 5 here.