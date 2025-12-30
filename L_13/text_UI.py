# ECOR 1031 Lab 13 - text UI module
# Remember to include type annotations for your functions

__author__ = "Ryan McCracken"
__student_number__ = "101375579"
import sort
import plot
import fit
import load_data as ld

import time
#==========================================#
# Place your script for your text_UI after this line
# You are allowed to create auxiliary functions
data = None
menu_prompt = f"""The available commands are:
    L)oad Data
    S)ort Data
    C)urve Fit
    H)istogram
    E)xit
Please enter a command: """


def load_data():
    global data
    file_name = input("Please enter the name of the file: ")
    attrib = input("Please enter the attribute to use as a filter: ")
    while attrib not in ld.VALID_ATTRIBUTES:
        attrib = input("Invalid attribute.\nPlease enter the attribute to use as a filter: ")
    if attrib != "All":
        value = input("Please enter the value of the attribute: ")
        data = ld.load_data(file_name, {attrib: value})
    else:
        data = ld.load_data(file_name, {"All": True})
    if len(data) != 0:
        data = ld.add_average(data)
    print("Data Loaded")

def sort_data():
    global data
    if not data:
        print("File not loaded. Please, load a file first.")
        return
    sort_key_prompt = "Please enter the attribute you want to use for sorting: \n 'Age', 'AvgGrade', 'StudyTime'\n "
    sort_key = input(sort_key_prompt)
    while sort_key not in {"Age", "AvgGrade", "StudyTime"}:
        sort_key = input("Invalid attribute.\n" + sort_key_prompt)
    order = input("Ascending (A) or Descending (D) order: ").strip().upper()
    while order not in {"A", "D"}:
        order = input("Invalid order.\nAscending (A) or Descending (D) order: ").strip().upper()
    val = sort.sort(data, order, sort_key)
    display = input("Do you want to display the data?: ")
    while display.strip().upper() not in {"Y", "N"}:
        display = input("Invalid input.\nDo you want to display the data?: ")
    if display.strip().upper() == "Y":
        for student in data:
            print(student)
    


def curve_fit():
    if not data:
        print("File not loaded. Please, load a file first.")
        return
    attribute = input("Please enter the attribute you want to use to find the best fit for AvgGrade: ")
    deg = input("Please enter the order of the polynomial to be fitted: ")
    result = fit.curve_fit(data, attribute, int(deg))
    print(result)

def histogram():
    if not data:
        print("File not loaded. Please, load a file first.")
        return
    attrib = input("Please enter the attribute you want to use for plotting: ")
    plot.histogram(data, attrib)

if __name__ == "__main__":
    end = False
    while not end:
        time.sleep(0.5)
        command = input(menu_prompt).strip().upper()
        if command == "L":
            load_data()
        elif command == "S":
            sort_data()
        elif command == "C":
            curve_fit()
        elif command == "H":
            histogram()
        elif command == "E":
            end = True
        else:
            print("Invalid command.")





