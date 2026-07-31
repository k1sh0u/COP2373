'''
In this assignment, you will utilize numpy to analyze student grades stored in a CSV file. You will perform various statistical calculations and operations to gain insights into the dataset. This assignment will help you practice data manipulation and analysis using numpy arrays.

Instructions:

Use your CSV file from your Programming Exercise CSV in Week 7. (The file should have at least 10 students in it, so rerun your code to have at least 10 if needed).
Load the data from the CSV file into a numpy array.
Print the first few rows of the dataset to understand its structure.
Calculate and print the following statistics for each exam (columns):
Mean (average) x
Median x
Standard deviationx
Minimum x
Maximumx
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

#importing my the CSV and numpy packages to use their functions
import csv
import numpy as np

# grades_to_array created to use the csv file we used and create a numpy array using the contents of the file.
def grades_to_array():

    #contents of csv file will be
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
    print(array)
    print("this is the mean of each exam (1st, 2nd, 3rd): ", np.mean(array,axis=0))
    print("this is the median of each exam (1st, 2nd, 3rd): ", np.median(array,axis=0))
    print("this is the min of each exam (1st, 2nd, 3rd): ", np.min(array,axis=0))
    print("this is the max of each exam (1st, 2nd, 3rd): ", np.max(array,axis=0))
    print("this is the standard deviation of each exam (1st, 2nd, 3rd): ", np.std(array,axis=0))
    print("\n")
    print("these are the statistics of all the exams")
    print("this is the mean of the all the exams", np.mean(array))
    print("this is the median of the all the exams", np.median(array))
    print("this is the min of the all the exams", np.min(array))
    print("this is the max of the all the exams", np.max(array))
    print("this is the standard deviation of the all the exams", np.std(array))
    print("\n")
    print(f"# of students that passed the first exam: {np.sum(array[:,0] >= 60, axis=0)}\n# of students failed the first exam: {np.sum(array[:,0] < 60)}")
    print(f"# of students that passed the second exam: {np.sum(array[:,1] >= 60, axis=0)}\n# of students failed the second exam: {np.sum(array[:,1] < 60)}")
    print(f"# of students that passed the third exam: {np.sum(array[:,2] >= 60, axis=0)}\n# of students failed the third exam: {np.sum(array[:,2] < 60)} ")
    print("\n")
    print(f"The overall passing percentage is {(np.sum(array >= 60) / array.size) * 100}%")


def main ():
    grades_array = grades_to_array()

    calculate_statistics(grades_array)

if __name__ == '__main__':
    main()