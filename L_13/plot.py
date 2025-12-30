# ECOR 1031 Lab 12 - plot module
# Remember to include type annotations for your functions

__author__ = "Ryan McCracken"
__student_number__ = "101375597"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt

def histogram(data: list[dict], key: str) -> int:
    try:
        float(data[0][key])
        numeric = True
    except (ValueError, TypeError, KeyError):
        numeric = False
    if numeric:
        max_value = data[0][key]
        values = []
        for entry in data:
            if key in entry:
                values.append(entry[key])
                if entry[key] > max_value:
                    max_value = entry[key]
        fig = plt.figure()
        plt.hist(values, bins=10, edgecolor='black')
        plt.title(f'Histogram of {key}')
        plt.xlabel(key)
        plt.ylabel('Frequency')
        plt.show()
        return max_value
    else:
        fig = plt.figure()
        plt.xlabel(key)
        plt.ylabel("Frequency")
        counts = {}
        for entry in data:
            if key in entry:
                key_value = entry[key]
                if key_value in counts:
                    counts[key_value] += 1
                else:
                    counts[key_value] = 1
        keys = list(counts.keys())
        frequencies = list(counts.values())
        plt.bar(keys, frequencies, color='blue', edgecolor='black')
        plt.title(f'Bar Chart of {key}')
        plt.show()
        return -1


# Do NOT include a main script in your submission
