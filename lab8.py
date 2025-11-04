# ECOR 1031 - Lab 8

__author__ = "Ryan McCracken"
__student_number__ = "101375579"

# ======================================================
# Exercise 1

# Type your function definition for Exercise 1 here.
def middle_way(list_a: list[int], list_b: list[int]) -> list[int]:
    """
    Return a new list containing the middle element of the two lists of 3 integers.
    
    Precondition: len(list_a) == 3 and len(list_b) == 3

    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([0, 1, 1], [2, 1, 2])
    [1, 1]
    >>> middle_way([5, 6, 7], [3, 1, 4])
    [6, 1]
    """
    return [list_a[1], list_b[1]]


# ======================================================
# Exercise 2

# Type your function definition for Exercise 2 here.
def make_ends(nums: list[int]) -> list[int]:
    """
    Return a new list containing the first and last elements of the input list.
    
    Precondition: len(nums) > 0
    
    >>> make_ends([1, 2, 3])
    [1, 3]
    >>> make_ends([1])
    [1, 1]
    >>> make_ends([7, 4, 6, 2, 5, 3, 1, 7])
    [7, 7]
    """
    return [nums[0], nums[-1]]

# ======================================================
# Exercise 3

# Type your function definition for Exercise 3 here.
def common_end(list_a: list[int], list_b: list[int]) -> bool:
    """
    Return True if the two input lists have the same first element or the same last element, or 
    if the first and last elements are the same of both lists.
    
    Preconditions: len(list_a) > 0 and len(list_b) > 0
    
    >>> common_end([1, 2, 3], [7, 3])
    True
    >>> common_end([1, 5, 8, 2, 6, 4], [1, 3, 5])
    True
    >>> common_end([1], [2])
    True
    >>> common_end([1, 2, 3], [4, 5, 6])
    False
    """
    return list_a[0] == list_b[0] or list_a[-1] == list_b[-1] or list_a[0] == list_a[-1] and list_b[0] == list_b[-1]

# ======================================================
# Exercise 4

# Type your function definition for Exercise 4 here.
def count_evens(nums: list[int]) -> int:
    """
    Return the number of even integers in the input list.
    
    Precondition: N/A
    
    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    count = 0
    for num in nums:
        count += (num % 2)^1
    return count

# ======================================================
# Exercise 5

# Type your function definition for Exercise 5 here.
def big_diff(nums: list[int]) -> int:
    """
    Return the difference between the largest and smallest values in the input list.
    
    Precondition: len(nums) > 1
    
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2])
    5
    >>> big_diff([2, 10, 7, 5, 4, 1])
    9
    """
    big = nums[0]
    small = nums[0]
    for num in range(1, len(nums)):
        if nums[num] > big:
            big = nums[num]
        elif nums[num] < small:
            small = nums[num]
    return big - small

# ======================================================
# Exercise 6

# Type your function definition for Exercise 6 here.
def has22(nums: list[int]) -> bool:
    """
    Return True if the input list contains a 2 next to a 2.
    
    Precondition: N/A

    >>> has22([1, 2, 2])
    True
    >>> has22([])
    False
    >>> has22([2])
    False
    >>> has22([1, 2, 1, 2])
    False
    """

    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

# ======================================================
# Exercise 7

# Type your function definition for Exercise 7 here.
def centered_average(nums: list[int]) -> float:
    """
    Return the average of nums, excluding the largest and smallest values.
    
    Precondition: len(nums) > 2

    >>> centered_average([1, 2, 3, 4, 100])
    3.0
    >>> centered_average([1, 1, 5, 5, 10, 7, 7])
    5.0
    >>> centered_average([5, 5, 5])
    5.0
    """
    big = max(nums)
    small = min(nums)
    total = 0
    for num in nums:
        total += num
    return (total - big - small) / (len(nums) - 2)

# ======================================================
# Exercise 8

# Type your function definition for Exercise 8 here.
def bank_statement(transactions: list[float]) -> list[float, float, float]:
    """
    Return a list containing the sum of the deposits, the sum of the withdrawals, and the current account balance, all rounded to two decimals.
    
    Precondition: len(transactions) > 0
    
    >>> bank_statement([100.0, -50.0, 25.0, -10.0])
    [125.0, -60.0, 65.0]
    >>> bank_statement([-20.0, -30.0, -10.0])
    [0.0, -60.0, -60.0]
    >>> bank_statement([199.9899999, -99.999999])
    [199.99, -100.0, 99.99]
    """
    deposits = 0.0
    withdrawals = 0.0
    for transaction in transactions:
        if transaction > 0:
            deposits += transaction
        else:
            withdrawals += transaction
    return [round(deposits, 2), round(withdrawals, 2), round(deposits + withdrawals, 2)]
# ======================================================
# Exercise 9

# Type your function definition for Exercise 9 here.
def reverse(lst: list) -> list:
    """
    Return a new list that is the reverse of the input list.
    
    Precondition: N/A
    
    >>> reverse([1, 2, 3])
    [3, 2, 1]
    >>> reverse(['a', 'b', 'c', 'd'])
    ['d', 'c', 'b', 'a']
    >>> reverse([])
    []
    """
    for i in range(len(lst) // 2):
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
    return lst