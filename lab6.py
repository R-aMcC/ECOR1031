# ECOR 1031 Lab 6

__author__ = "Ryan McCracken"
__student_number__ = "101375597"
import doctest
# ======================================================
# Exercise 1
def add_up(num: int) -> float:
    """Return the sum of the series 1/num + 2/(num-1) + ... + num/1.
    
    Preconditions: num > 0
    
    >>> add_up(1)
    1.0
    >>> add_up(2)
    2.5
    >>> add_up(5)
    8.7
    """
    total = 0
    for i in range(num):
        total += (i + 1) / (num - i)
    return total
# Type your function definition for Exercise 1 here.

# ======================================================
# Exercise 2
def fib(n: int) -> int:
    """Return the nth Fibonacci number.
    
    Preconditions: n >= 0
    
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(7)
    13
    """
    if n <= 1:
        return n
    else:
        second_last = 0
        last = 1
        for _ in range(2, n):
            last, second_last = last + second_last, last
        return last + second_last

# Type your function definition for Exercise 2 here.

# ======================================================
# Exercise 3
def years_to_double(initial: float, rate: float) -> int:
    """Return the amount of time in years it will take for an initial amount to double given an interest rate.
    
    Preconditions: initial > 0, rate > 0
    
    >>> years_to_double(1, 1)
    70
    >>> years_to_double(100, 10)
    8
    >>> years_to_double(10000, 5)
    15
    """
    total = initial
    years = 0
    while total < 2 * initial:
        total *= 1 + rate / 100
        years += 1
    return years
# Type your function definition for Exercise 3 here.

# ======================================================
# Exercise 4
def replicate(string: str) -> str:
    """Return the input string repeated the number of times equal to its length.

    Preconditions: N/A
    
    >>> replicate("abc")
    'abcabcabc'
    >>> replicate("hello")
    'hellohellohellohellohello'
    >>> replicate("x")
    'x'
    """
    result = ""
    for _ in string:
        result += string
    return result

# Type your function definition for Exercise 4 here.

# ======================================================
# Exercise 5
def repeat_separator(string: str, separator: str, count: int) -> str:
    """Return a string with the input string repeated count times, separated by the separator string.
    
    Preconditions: count > 0
    
    >>> repeat_separator("abc", "-", 3)
    'abc-abc-abc'
    >>> repeat_separator("hello", " ", 2)
    'hello hello'
    >>> repeat_separator("x", ",", 1)
    'x'
    """
    result = string
    for _ in range(1, count):
        result += separator + string
    return result
# Type your function definition for Exercise 5 here.

# ======================================================
# Exercise 6
def has_pair(string: str, char: str) -> bool:
    """Return True if the input string contains two consecutive occurrences of the input character
    
    Preconditions: len(char) == 1
    
    >>> has_pair("hello", "l")
    True
    >>> has_pair("hello", "e")
    False
    >>> has_pair("abcabc", "a")
    False
    """
    for i in range(len(string) - 1):
        if string[i] == char and string[i + 1] == char:
            return True
    return False
# Type your function definition for Exercise 6 here.

#=======================================================
# Write your main script here
def test_add_up() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert abs(add_up(1) - 1.0) < 0.0001, f"  - add_up(1) should be 1.0, is {add_up(1)}"
        successful_tests += 1
    except AssertionError as _:
        pass
    try:
        tests += 1
        assert abs(add_up(2) - 2.5) < 0.0001, f"  - add_up(2) should be 2.5, is {add_up(2)}"
        successful_tests += 1
    except AssertionError as _:
        pass
    try:
        tests += 1
        assert abs(add_up(5) - 8.7) < 0.0001, f"  - add_up(5) should be 8.7, is {add_up(5)}"
        successful_tests += 1
    except AssertionError as _:
        pass
    print(f"- add_up tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

def test_fib() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert fib(0) == 0, f"fib(0) should be 0, is {fib(0)}"
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert fib(1) == 1, f"fib(1) should be 1, is {fib(1)}"
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert fib(7) == 13, f"fib(7) should be 13, is {fib(7)}"
        successful_tests += 1
    except AssertionError:
        pass
    print(f"- fib tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

def test_years_to_double() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert years_to_double(1, 1) == 70, f"years_to_double(1, 1) should be 70, is {years_to_double(1, 1)}"
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert years_to_double(100, 10) == 8, f"years_to_double(100, 10) should be 8, is {years_to_double(100, 10)}"
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert years_to_double(10000, 5) == 15, f"years_to_double(10000, 5) should be 15, is {years_to_double(10000, 5)}"
        successful_tests += 1
    except AssertionError:
        pass
    print(f"- years_to_double tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

def test_replicate() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert replicate("abc") == "abcabcabc", f'replicate("abc") should be "abcabcabc", is {replicate("abc")}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert replicate("hello") == "hellohellohellohellohello", f'replicate("hello") should be "hellohellohellohellohello", is {replicate("hello")}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert replicate("x") == "x", f'replicate("x") should be "x", is {replicate("x")}'
        successful_tests += 1
    except AssertionError:
        pass
    print(f"- replicate tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

def test_repeat_separator() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert repeat_separator("abc", "-", 3) == "abc-abc-abc", f'repeat_separator("abc", "-", 3) should be "abc-abc-abc", is {repeat_separator("abc", "-", 3)}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert repeat_separator("hello", " ", 2) == "hello hello", f'repeat_separator("hello", " ", 2) should be "hello hello", is {repeat_separator("hello", " ", 2)}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert repeat_separator("x", ",", 1) == "x", f'repeat_separator("x", ",", 1) should be "x", is {repeat_separator("x", ",", 1)}'
        successful_tests += 1
    except AssertionError:
        pass
    print(f"- repeat_separator tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

def test_has_pair() -> tuple[int, int]:
    tests = 0
    successful_tests = 0
    try:
        tests += 1
        assert has_pair("hello", "l") == True, f'has_pair("hello", "l") should be True, is {has_pair("hello", "l")}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert has_pair("hello", "e") == False, f'has_pair("hello", "e") should be False, is {has_pair("hello", "e")}'
        successful_tests += 1
    except AssertionError:
        pass
    try:
        tests += 1
        assert has_pair("abcabc", "a") == False, f'has_pair("abcabc", "a") should be False, is {has_pair("abcabc", "a")}'
        successful_tests += 1
    except AssertionError:
        pass
    print(f"- has_pair tests passed. ({successful_tests}/{tests})")
    return tests, successful_tests

if __name__ == "__main__":

    print("""
==================================
Running tests...""")
    total_tests, successful_tests = 0, 0
    t, s = test_add_up()
    total_tests += t
    successful_tests += s
    t, s = test_fib()
    total_tests += t
    successful_tests += s
    t, s = test_years_to_double()
    total_tests += t
    successful_tests += s
    t, s = test_replicate()
    total_tests += t
    successful_tests += s
    t, s = test_repeat_separator()
    total_tests += t
    successful_tests += s
    t, s = test_has_pair()
    total_tests += t
    successful_tests += s
    print(f"({successful_tests}/{total_tests}) tests passed. \n==================================")