# ECOR 1031 - Lab 9

__author__ = "Ryan McCracken"
__student_number__ = "101375579"

# ======================================================
# Exercise 1
def make_pi() -> list[int]:
    """
    Return a list that contains the first three digits of pi.
    
    Preconditions: None

    >>> make_pi()
    [3, 1, 4]
    """
    return [3, 1, 4]
# Type your function definition for Exercise 1 here.

# ======================================================
# Exercise 2
def sum_list(lst: list[int]) -> list[int]:
    """
    Return a list containing the sum, length, and average of the input list of numbers.
    
    Preconditions: None
    >>> sum_list([1, 2, 3, 4, 5])
    [15, 5, 3.0]
    
    >>> sum_list([])
    [0, 0, 0]

    >>> sum_list([-10, -20, 30])
    [0, 3, 0.0]
    """
    total = 0
    length = len(lst)
    for e in lst:
        total += e
    return [total, length, total / length if length > 0 else 0]
# Type your function definition for Exercise 2 here.

# ======================================================
# Exercise 3
def sum13(lst: list[int]) -> int:
    """
    Return the sum of the numbers in the input list,
    excluding any number that is 13 and any number that comes immediately after a 13.

    Preconditions: None
    >>> sum13([1, 2, 2, 1])
    6
    >>> sum13([1, 2, 13, 2, 1, 13])
    4
    >>> sum13([])
    0
    """
    total = 0
    for i in range(len(lst)):
        if not (lst[i] == 13 or (i > 0 and lst[i - 1] == 13)):
            total += lst[i]
    return total
# Type your function definition for Exercise 3 here.

# ======================================================
# Exercise 4
def sum15(lst: list[int]) -> int:
    """
    Return the sum of the numbers in the input list, excluding any numbers that come between 1 and the next 5
    
    Preconditions: None
    >>> sum15([1, 2, 3, 5, 4])
    4
    >>> sum15([1, 2, 1, 5, 5])
    5
    >>> sum15([])
    0
    """
    total = 0
    i = 0
    count = True
    while i < len(lst):
        if lst[i] == 1 and count:
            count = False
        elif lst[i] == 5 and not count:
            count = True
        elif count:
            total += lst[i]
        i += 1
    return total

# Type your function definition for Exercise 4 here.

# ======================================================
# Exercise 5
def divisors(n : int) -> list[int]:
    """
    Return a list of all divisors of n

    Precondition: n > 0

    >>> divisors(6)
    [1, 2, 3, 6]

    >>> divisors(15)
    [1, 3, 5, 15]

    >>> divisors(1)
    [1]
    """
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs += [i]
    return divs + [abs(n)]
# Type your function definition for Exercise 5 here.

# ======================================================
# Exercise 6
def no_evens_zero(lst: list[int]) -> None:
    """
    Return None. Modify the input list by removing all even numbers including 0.

    Precondition: None

    >>> lst = [1, 2, 3, 4, 5]
    >>> no_evens_zero(lst)
    >>> lst
    [1, 3, 5]

    >>> lst = [2, 4, 6, 8]
    >>> no_evens_zero(lst)
    >>> lst
    []

    >>> lst = []
    >>> no_evens_zero(lst)
    >>> lst
    []

    """
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            del lst[i]
        else:
            i += 1
# Type your function definition for Exercise 6 here.

# ======================================================
# Exercise 7
def double_odd_index(lst: list[int]) -> None:
    """
    Return None. Modify the input list by doubling the values at odd indices.
    
    Precondition: None
    
    >>> lst = [1, 2, 3, 4, 5]
    >>> double_odd_index(lst)
    >>> lst
    [1, 4, 3, 8, 5]

    >>> lst = [10, 20, 30]
    >>> double_odd_index(lst)
    >>> lst
    [10, 40, 30]
    
    >>> lst = []
    >>> double_odd_index(lst)
    >>> lst
    []

    """
    for i in range (1, len(lst), 2):
        lst[i] *= 2
# Type your function definition for Exercise 7 here.

# ======================================================
# Exercise 8
def no_duplicates(lst: list[int]) -> list[int]:
    """
    Return a new list containing the elements of the input list with duplicates removed.
    Precondition: None
    >>> no_duplicates([1, 2, 2, 3, 4, 4, 4])
    [1, 2, 3, 4]

    >>> no_duplicates([5, 5, 5, 5, 5])
    [5]

    >>> no_duplicates([])
    []
    """
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst += [item]
    return new_lst

# Type your function definition for Exercise 8 here.
