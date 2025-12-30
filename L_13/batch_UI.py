# ECOR 1031 Lab 13 - batch UI module
# Remember to include type annotations for your functions

__author__ = "Ryan McCracken"
__student_number__ = "101375579"

import sort
import plot
import fit
import load_data as ld

#==========================================#
# Place your script for your batch_UI after this line
# You are allowed to create auxiliary functions



def batch_UI(commands: list[str]) -> None:
    data = None
    for command in commands:
        args = command.strip().split(';')
        if len(args) == 0:
            continue
        print(f"{command}")
        cmd_type = args[0].strip().upper()
        if cmd_type == "L":
            filename = args[1].strip()
            attrib = args[2].strip()
            if attrib == "All":
                attrib_value = True
            else:
                attrib_value = args[3].strip()
            data = ld.load_data(filename, {attrib: attrib_value})
            if len(data) != 0:
                data = ld.add_average(data)
            print("Data Loaded")
        elif cmd_type == "S":
            if not data:
                print("File not loaded. Please, load a file first.")
                continue
            sort_key = args[1].strip()
            order = args[2].strip().upper()
            val = sort.sort(data, order, sort_key)
            display = args[3].strip().upper()
            if display == "Y":
                for student in data:
                    print(student)
        elif cmd_type == "C":
            if not data:
                print("File not loaded. Please, load a file first.")
                continue
            attribute = args[1].strip()
            deg = int(args[2].strip())
            result = fit.curve_fit(data, attribute, deg)
            print(result)
        elif cmd_type == "H":
            if not data:
                print("File not loaded. Please, load a file first.")
                continue
            attrib = args[1].strip()
            plot.histogram(data, attrib)
        elif cmd_type == "E":
            return
        else:
            print("Invalid command.")

if __name__ == "__main__":
    file_name = input("Please enter the name of the file where your commands are stored: ")
    file = open(file_name, 'r')
    commands = []
    for line in file:
        commands.append(line.strip())
    file.close()
    batch_UI(commands)


