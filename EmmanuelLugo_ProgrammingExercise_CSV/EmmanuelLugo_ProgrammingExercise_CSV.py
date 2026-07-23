import csv

def write_to_csv_file():
    with open('../EmmanuelLugo_ProgrammingExercise_12/grades.csv', 'w') as file:
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



