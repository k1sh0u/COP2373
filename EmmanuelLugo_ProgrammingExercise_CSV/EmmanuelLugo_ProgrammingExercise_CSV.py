
'''
An instructor teaches a class in which each student takes three exams. The instructor would like to store this information in a file named grades.csv for later use. Create a program that allows an instructor to input how many students they want to enter. Then enter each student’s first name and last name as strings and the student’s three exam grades as integers. Use the csv module to write each record into the grades.csv file and have a header of First Name, Last Name, Exam 1, Exam 2 and Exam3. Each student should be a record in the grades.csv file.

Once the file is created, create a separate program to read the grades.csv file and display the data in tabular format. Implement the with keyword. You may need to refer back to Chapter 5 for formatting.

Each of these 2 programs should be separate functions so you have at least two functions for this assignment, but you can have more.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.

***The .csv file for this assignment should also be in your repository.
'''





import csv
def write_to_csv_file():
    with open('grades.csv', 'w') as file:
        write_data = file.write("First Name, Last Name, Exam 1, Exam 2, Exam3\n")

        while True:
            try:
                student_count = int(input("Enter count of students: "))
                if student_count <= 0:
                    print("Please enter a positive count of students")
                    continue
                break

            except ValueError:
                print("Please enter a valid count of student.")

        for i in range(student_count):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam_1 = int(input("Enter exam 1: "))
            exam_2 = int(input("Enter exam 2: "))
            exam_3 = (input("Enter exam 3: "))

            row = f"{first_name},{last_name},{exam_1},{exam_2},{exam_3},"
            file.write(row)

def read_csv_file():
    with open('grades.csv', 'r') as file:
        entry = file.readlines()
    full_content = ",".join(entry)
    items = full_content.strip().split(',')

    for i in range(0, len(items), 5):
        row = items[i:i+5]
        if len(row) == 5:
            print(f"{row[0].strip():<15}{row[1].strip():<15}{row[2]:>10}{row[3]:>10}{row[4]:>10}")


write_to_csv_file()



