# ECOR 1031 - Lab 11

__author__ = "Ryan McCracken"
__student_number__ = "101375597"

#==========================================#
# If you want to define auxiliary functions
# to make your code more modular, place them here
VALID_ATTRIBUTES = {"School", "Age", "Failures", "Health", "All"}
#==========================================#
# Place your load_data function after this line
def load_data(filename: str, filter: dict) -> list[dict]:
    """
    Return a list of dictionaries representing student data from the CSV file filtered based on the passed filter.

    Precondition:
        - `filename` refers to a valid CSV file with a header matching the
          fields: School, ID, Age, StudyTime, Failures, Health, Absences,
          FallGrade, WinterGrade
        - `filter` contains exactly one key from:
          {"School", "Age", "Failures", "Health", "All"}.

    >>> load_data("students.csv", {"School": "GP"})
    [{'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3,
      'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
     {'ID': 2, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3,
      'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}, ...]

    >>> load_data("students.csv", {"Age": 15})
    [{'School': 'GP', 'ID': 3, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3,
      'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8},
     {'School': 'GP', 'ID': 4, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5,
      'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14}, ...]

    >>> load_data("students.csv", {"All": True})
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0,
      'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6},
     {'School': 'GP', 'ID': 2, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0,
      'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5},
     ...]
    """
    file = open(filename, 'r')
    data = []
    header = None
    filter_key = list(filter.keys())[0]
    filter_value = str(filter[filter_key])
    # print(f"filter key: {filter_key}, filter value: {filter_value}")
    if filter_key not in VALID_ATTRIBUTES:
        print("Invalid Value")
        file.close()
        return []
    try:
        for line in file:
            if not header:
                # print(f"Header line: {line.strip()}")
                header = line.strip().split(',')
                if filter_key == "All":
                    # print("No filtering applied")
                    filter_key = None
                else:
                    filter_key = header.index(filter_key)
                    # print(f"Filter key index: {filter_key}, Filter value: {filter_value}")
                # print(f"Header: {header}")
            else:
                values = line.strip().split(',')
                if filter_key != None and values[filter_key] != filter_value:
                    continue
                else:
                    entry = {}
                    for i in range(len(header)):
                        if i != filter_key:
                            try:
                                if values[i].isdigit():
                                    entry[header[i]] = int(values[i])
                                else:
                                    entry[header[i]] = float(values[i])
                            except:
                                entry[header[i]] = values[i]
                    data.append(entry)
    except:
        print("An error occurred while reading the file.")
    finally:
        file.close()
    return data

#==========================================#
# Place your add_average function after this line
def add_average(student_data: list[dict]) -> list[dict]:
    """
    Return the student_data list with an added AvgGrade rounded to two decimal places
    for each student dictionary.

    Precondition: Each dictionary contains the keys "FallGrade" and "WinterGrade"
    with integer values.

    >>> data = [
    ...     {"School": "GP", "ID": 1, "Age": 18, "StudyTime": 2.5, "Failures": 0,
    ...      "Health": 3, "Absences": 6, "FallGrade": 5, "WinterGrade": 6},
    ...     {"School": "GP", "ID": 2, "Age": 17, "StudyTime": 2, "Failures": 0,
    ...      "Health": 3, "Absences": 4, "FallGrade": 5, "WinterGrade": 5}
    ... ]
    >>> add_average(data)
    [{'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0,
      'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6,
      'AvgGrade': 5.5},
     {'School': 'GP', 'ID': 2, 'Age': 17, 'StudyTime': 2, 'Failures': 0,
      'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5,
      'AvgGrade': 5.0}]

    >>> add_average([
    ...     {"School": "GP", "ID": 4, "Age": 15, "StudyTime": 3, "Failures": 0,
    ...      "Health": 5, "Absences": 2, "FallGrade": 15, "WinterGrade": 14}
    ... ])
    [{'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3, 'Failures': 0,
      'Health': 5, 'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14,
      'AvgGrade': 14.5}]

    >>> add_average([
    ...     {"School": "GP", "ID": 9, "Age": 15, "StudyTime": 2, "Failures": 0,
    ...      "Health": 1, "Absences": 0, "FallGrade": 16, "WinterGrade": 18}
    ... ])
    [{'School': 'GP', 'ID': 9, 'Age': 15, 'StudyTime': 2, 'Failures': 0,
      'Health': 1, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 18,
      'AvgGrade': 17.0}]
    """
    for student in student_data:
        student["AvgGrade"] = round((student["FallGrade"] + student["WinterGrade"]) / 2, 2)
    return student_data
