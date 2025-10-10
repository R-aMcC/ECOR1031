# ECOR 1031 Lab 6

__author__ = "Ryan McCracken"
__student_number__ = "101375597"

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
if __name__ == "__main__":
    while True:
        print("============================\nMenu:")
        choice = input("""
1. Add up series
2. Fibonacci
3. Years to double
4. Replicate
5. Repeat separator
6. Has pair
7. Exit
Enter your choice: """)
        if choice == "1":
            num = int(input("Enter a positive integer: "))
            print(f"The sum of the series is: {add_up(num)}")
        elif choice == "2":
            n = int(input("Enter a non-negative integer: "))
            print(f"The {n}th Fibonacci number is: {fib(n)}")
        elif choice == "3":
            initial = float(input("Enter the initial amount (greater than 0): "))
            rate = float(input("Enter the interest rate (greater than 0): "))
            print(f"It will take {years_to_double(initial, rate)} years to double the amount.")
        elif choice == "4":
            string = input("Enter a string: ")
            print(f"The replicated string is: {replicate(string)}")
        elif choice == "5":
            string = input("Enter the string to repeat: ")
            separator = input("Enter the separator string: ")
            count = int(input("Enter the number of times to repeat (greater than 0): "))
            print(f"The result is: {repeat_separator(string, separator, count)}")
        elif choice == "6":
            string = input("Enter a string: ")
            char = input("Enter a single character: ")
            print(f"Does the string have a pair of '{char}'? {has_pair(string, char)}")
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
