# ECOR 1031 Lab 7

__author__ = "Ryan McCracken"
__student_number__ = "101375597"
import lab6 as l

# ======================================================
# Type your function definition for test_add_up() here.
def test_add_up():
    test_cases = [[1, 1.0], [2, 2.5], [5, 8.7], [10, 22.2186508], [3, 4.3333333]]

    tests = 0
    successful_tests = 0
    for case in test_cases:
        try:
            tests += 1
            result = l.add_up(case[0])
            assert abs(result-case[1]) < 0.0001, f"add_up({case[0]}) should be {case[1]}, is {result}"
            assert isinstance(result, float), f"add_up({case[0]}) should be a float, is {type(result)}"
            successful_tests += 1
        except AssertionError as e:
            print(f" - Test failed in add_up: {e}")
    return tests - successful_tests

# ======================================================
# Type your function definition for test_years_to_double() here.
def test_years_to_double():
    test_cases = [[[1, 1], 70], [[100, 10], 8], [[10000, 5], 15], [[100, 100], 1], [[100, 0.01], 6932]]
    tests = 0
    successful_tests = 0
    for case in test_cases:
        try:
            tests += 1
            result = l.years_to_double(case[0][0], case[0][1])
            assert result == case[1], f"years_to_double({case[0][0]}, {case[0][1]}) should be {case[1]}, is {result}"
            assert isinstance(result, int), f"years_to_double({case[0][0]}, {case[0][1]}) should be an int, is {type(result)}"
            successful_tests += 1
        except AssertionError as e:
            print(f" - Test failed in years_to_double: {e}")
    return tests - successful_tests

# ======================================================
# Type your function definition for test_replicate() here.
def test_replicate():
    test_cases = [["abc", "abcabcabc"], ["hello", "hellohellohellohellohello"], ["x", "x"], ["", ""], ["longstring", "longstringlongstringlongstringlongstringlongstringlongstringlongstringlongstringlongstringlongstring"]]
    tests = 0
    successful_tests = 0
    for case in test_cases:
        try:
            tests += 1
            result = l.replicate(case[0])
            assert result == case[1], f'replicate("{case[0]}") should be "{case[1]}", is "{result}"'
            assert isinstance(result, str), f'replicate("{case[0]}") should be a string, is {type(result)}'
            successful_tests += 1
        except AssertionError as e:
            print(f" - Test failed in replicate: {e}")
    return tests - successful_tests
# ======================================================
# Type your function definition for test_repeat_separator() here.
def test_repeat_separator():
    test_cases = [[["abc", "---", 3], "abc---abc---abc"], [["hello", " ", 2], "hello hello"], [["x", ",", 1], "x"], [["yes", "", 4], "yesyesyesyes"], [["", "-", 5], "----"]]
    tests = 0
    successful_tests = 0
    for case in test_cases:
        try:
            tests += 1
            result = l.repeat_separator(case[0][0], case[0][1], case[0][2])
            assert result == case[1], f'repeat_separator("{case[0][0]}", "{case[0][1]}", {case[0][2]}) should be "{case[1]}", is "{result}"'
            assert isinstance(result, str), f'repeat_separator("{case[0][0]}", "{case[0][1]}", {case[0][2]}) should be a string, is {type(result)}'
            successful_tests += 1
        except AssertionError as e:
            print(f" - Test failed in repeat_separator: {e}")
    return tests - successful_tests

# ======================================================
# Type your function definition for test_has_pair() here.
def test_has_pair():
    test_cases = [["hello", "l", True], ["hello", "e", False], ["abcabc", "a", False], ["", "a", False], ["Aa", "a", False]]
    tests = 0
    successful_tests = 0
    for case in test_cases:
        try:
            tests += 1
            result = l.has_pair(case[0], case[1])
            assert result == case[2], f'has_pair("{case[0]}", "{case[1]}") should be {case[2]}, is {result}'
            assert isinstance(result, bool), f'has_pair("{case[0]}", "{case[1]}") should be a bool, is {type(result)}'
            successful_tests += 1
        except AssertionError as e:
            print(f" - Test failed in has_pair: {e}")

    return tests - successful_tests
# =======================================================
# Write your main script here
try:
    assert __name__ == "__main__"
    print("""
==================================
Running tests...""")
    print("Testing add_up()...")
    failed_tests = test_add_up()
    print(f"- {failed_tests} tests failed")
    print("Testing has_pair()...")
    f = test_has_pair()
    print(f"- {f} tests failed")
    print("Testing repeat_seperator()...")
    failed_tests += f
    f = test_repeat_separator()
    print(f"- {f} tests failed")
    failed_tests += f
    print(f"Testing replicate()...")
    f = test_replicate()
    print(f"- {f} tests failed")
    failed_tests += f
    print("Testing years_to_double()")
    f = test_years_to_double()
    print(f"- {f} tests failed")
    failed_tests += f
    print(f"Total: {failed_tests} tests failed... \n ==================================")

except AssertionError:
    pass
