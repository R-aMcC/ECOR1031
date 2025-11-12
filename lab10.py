# ECOR 1031 - Lab 10

__author__ = "Ryan McCracken"
__student_number__ = "101375579"

# ======================================================
# No submission is needed for Exercise 1

# ======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.
def average(lst: list[(int, int, int)]) -> list[(int, int, int)]:
    """
    Return a new list of tuples where each value in the tuple is the integer average of the values 
    in the tuple at that index in the input list.

    Preconditions: None
    
    >>> average( [(1, 2, 3), (4, 5, 6), (7, 8, 9)] )
    [(2, 2, 2), (5, 5, 5), (8, 8, 8)]

    >>> average([])
    []

    >>> average([(0, 0, 5), (8, 100, 5), (13, 23, 9), (20, 30, 40)])
    [(1, 1, 1), (37, 37, 37), (15, 15, 15), (30, 30, 30)]

    """
    
    new_list = []
    for tup in lst:
        avg = (tup[0] + tup[1] + tup[2]) // 3
        new_list.append((avg, avg, avg)) 
    return new_list
# ======================================================
# No submission is needed for Exercise 3

# ======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.
def sum_x(input_set : set[(float, float)]) -> float:
    """
    Return the sum of the x coordinates of all the points in the input set.
    
    Preconditions: None
    
    >>> sum_x({(1, 2), (3, 4), (5, 6)})
    9

    >>> sum_x(set())
    0

    >>> sum_x({(1.5, 2.3), (-4.0, -3.2), (-0.5, 0.5)})
    -3.0

    """
    total = 0
    for x, y in input_set:
        total += x
    return total
# ======================================================
# No submission is needed for Exercise 5

# ======================================================
# Exercise 6

# Type your function definition for Exercise 6 here.
def frequency(lst = list[str]) -> dict[str, int]:
    """
    Return a dictionary mapping each unique string in the input list to the number of times it appears in the list.
    
    Preconditions: None
    
    >>> frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
    {'apple': 3, 'banana': 2, 'orange': 1}

    >>> frequency([])
    {}

    >>> frequency(['cat', 'dog', 'fish', 'rabbit', 'turtle', 'chinchilla'])
    {'cat': 1, 'dog': 1, 'fish': 1, 'rabbit': 1, 'turtle': 1, 'chinchilla': 1}

    """
    freq_dict = {}
    for element in lst:
        freq_dict[element] = freq_dict.get(element, 0) + 1 # Get the current count or 0 if not present and add 1
    return freq_dict
# ======================================================
# Exercise 7

# Type your function definition for Exercise 7 here.
def merge_dict(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    """
    Return a new dictionary that contains the values from both input dictionaries with their values summed for any duplicate keys.
    
    Preconditions: None
    
    >>> merge_dict({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    {'a': 1, 'b': 5, 'c': 4}

    >>> merge_dict({ "the": 3, "one": 2, "two": 1 }, { "then": 1, "one": 2, "the": 1 })
    {'the': 4, 'one': 4, 'two': 1, 'then': 1}

    >>> merge_dict({}, {'x': 10, 'y': 20})
    {'x': 10, 'y': 20}

    >>> merge_dict({}, {})
    {}
    """
    m_dict = dict1.copy()
    for key, value in dict2.items():
        m_dict[key] = m_dict.get(key, 0) + value
    return m_dict




# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)