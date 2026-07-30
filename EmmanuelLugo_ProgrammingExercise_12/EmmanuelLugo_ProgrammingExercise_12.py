'''
In this assignment, you will utilize numpy to analyze student grades stored in a CSV file. You will perform various statistical calculations and operations to gain insights into the dataset. This assignment will help you practice data manipulation and analysis using numpy arrays.

Instructions:

Use your CSV file from your Programming Exercise CSV in Week 7. (The file should have at least 10 students in it, so rerun your code to have at least 10 if needed).
Load the data from the CSV file into a numpy array.
Print the first few rows of the dataset to understand its structure.
Calculate and print the following statistics for each exam (columns):
Mean (average)
Median
Standard deviation
Minimum
Maximum
Calculate and print the overall statistics for the entire dataset (all exams combined):
Mean (average) grade across all exams
Median grade across all exams
Standard deviation of grades across all exams
Minimum grade across all exams
Maximum grade across all exams
Determine and print the number of students who passed and failed each exam. Consider a passing grade as 60 or above.
Calculate and print the overall pass percentage across all exams.
You should have at least two functions, but you can have more.
'''
import csv

import numpy as np

def grades_to_array():
    grades_list = []

    with open('grades.csv', "r") as csv_file:
     lines = csv_file.readlines()

    raw_data = lines[1].strip().split(",")
    raw_data = [item.strip() for item in raw_data if item.strip() != ""]
    for i in range(0,len(raw_data), 5):
        section = raw_data[i:i+5]
        if len(section) == 5:
            exams = [float(section[2]), float(section[3]), float(section[4])]
            grades_list.append(exams)

    return np.array(grades_list)

def calculate_statistics(array):
    print(array[:3])

   
main()


