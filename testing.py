from lab9 import sum13


def test_sum13():
    cases = [
        ([1, 2, 2, 1], 6),
        ([1, 2, 13, 2, 1, 13], 4),
        ([], 0),
        ([13, 1, 2, 3], 5),
        ([1, 13, 2, 13, 3], 1),
        ([13, 13, 13], 0),
        ([1, 2, 3, 4, 5], 15),
        ([13, 13, 1, 2, 3, 4, 5], 14) 
    ]
    fails = 0
    total = 0
    for lst, expected in cases:
        total += 1
        try:
            assert sum13(lst) == expected, f"sum13({lst}) should be {expected}"
        except AssertionError as e:
            print(f"Test {total} failed:", e)
            fails += 1
    print(f"Total tests: {total}, Failed tests: {fails}")


if __name__ == "__main__":
    test_sum13()
