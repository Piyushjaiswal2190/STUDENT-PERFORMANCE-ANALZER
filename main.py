
#  STUDENT PERFORMANCE ANALYZER
subjects = ["MAT1003", "CSE1021", "ENG1004", "CHY1001"]
students = []
FILE_NAME = "students.txt"
# ================= CALCULATIONS =================
def total_marks(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def average_marks(marks):
    return total_marks(marks) / len(marks)

def highest_marks(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

def lowest_marks(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest

def grade(mark):
    if mark >= 90:
        return "S Grade - 10 Points"
    elif mark >= 80:
        return "A Grade - 9 Points"
    elif mark >= 70:
        return "B Grade - 8 Points"
    elif mark >= 60:
        return "C Grade - 7 Points"
    elif mark >= 50:
        return "D Grade - 6 Points"
    elif mark >= 40:
        return "E Grade - 5 Points"
    else:
        return "F Grade - 0 Points"

def grade_point(mark):
    if mark >= 90:
        return 10
    elif mark >= 80:
        return 9
    elif mark >= 70:
        return 8
    elif mark >= 60:
        return 7
    elif mark >= 50:
        return 6
    elif mark >= 40:
        return 5
    else:
        return 0
    
# ================= FEEDBACK =================
def subject_feedback(subject, mark):
    if mark < 40:
        print(subject, ": Need improvement.")
        print("Feedback: Revise basic concepts and practice daily.")
    elif mark < 60:
        print(subject, ": Average performance.")
        print("Feedback: Solve more questions and revise regularly.")
    elif mark < 75:
        print(subject, ": Good performance.")
        print("Feedback: Improve accuracy and weak topics.")
    elif mark < 90:
        print(subject, ": Very good performance.")
        print("Feedback: Practice difficult questions.")
    else:
        print(subject, ": Excellent performance.")
        print("Feedback: Keep maintaining this performance.")

def attendance_feedback(attendance):
    if attendance < 75:
        print("Attendance Warning: Below 75%.")
        print("Attend classes regularly.")
    elif attendance < 85:
        print("Attendance is acceptable.")
        print("Try to attend more classes.")
    else:
        print("Excellent attendance. Keep it up.")

def overall_feedback(average):
    if average < 40:
        print("Performance needs serious improvement.")
        print("Focus on basic concepts and daily practice.")
    elif average < 60:
        print("Performance is average.")
        print("Prepare a proper study timetable.")
    elif average < 75:
        print("Performance is good.")
        print("Focus more on weak subjects.")
    elif average < 90:
        print("Performance is very good.")
        print("Practice advanced questions.")
    else:
        print("Excellent performance.")
        print("Keep working hard and maintain your score.")

def study_plan(average):
    print("\n========== STUDY PLAN ==========")

    if average < 40:
        print("Study 2 hours daily.")
        print("Revise basic concepts.")
    elif average < 60:
        print("Study 1.5 hours daily.")
        print("Revise classroom notes.")
    elif average < 75:
        print("Study 1 hour daily.")
        print("Focus on difficult topics.")
    else:
        print("Revise regularly.")
        print("Practice previous-year questions.")


# ================= FILE HANDLING =================

def save_student(student):
    file = open(FILE_NAME, "a")

    file.write(student["name"] + "|")
    file.write(student["roll_no"] + "|")

    for mark in student["marks"]:
        file.write(str(mark) + "|")

    file.write(str(student["attendance"]) + "\n")

    file.close()

def save_all_students():
    file = open(FILE_NAME, "w")

    for student in students:
        file.write(student["name"] + "|")
        file.write(student["roll_no"] + "|")

        for mark in student["marks"]:
            file.write(str(mark) + "|")

        file.write(str(student["attendance"]) + "\n")

    file.close()

def load_students():
    try:
        file = open(FILE_NAME, "r")
        for line in file:
            data = line.strip().split("|")

            if len(data) == 7:
                student = {
                    "name": data[0],
                    "roll_no": data[1],
                    "marks": [
                        int(data[2]),
                        int(data[3]),
                        int(data[4]),
                        int(data[5])
                    ],
                    "attendance": int(data[6]) }
                students.append(student)
        file.close()

    except FileNotFoundError:
        file = open(FILE_NAME, "w")
        file.close()

# ================= SEARCH =================

def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None

# ================= ADD STUDENT =================

def add_student():
    print("\n========== ADD STUDENT ==========")

    name = input("Enter your Name: ")
    roll_no = input("Enter your Roll No: ")

    if find_student(roll_no) != None:
        print("Roll No already exists.")
        return
    marks = []
    for subject in subjects:
        mark = int(input("Enter " + subject + " marks: "))

        while mark < 0 or mark > 100:
            print("Marks should be between 0 and 100.")
            mark = int(input("Enter " + subject + " marks: "))

        marks.append(mark)
    attendance = int(input("Enter attendance percentage: "))

    while attendance < 0 or attendance > 100:
        print("Attendance should be between 0 and 100.")
        attendance = int(input("Enter attendance percentage: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "attendance": attendance}

    students.append(student)
    save_student(student)

    print("\nStudent added successfully!")
    print("Data saved permanently.")

# ================= STUDENT REPORT =================

def display_report():
    print("\n========== STUDENT REPORT ==========")

    roll_no = input("Enter Roll No: ")
    student = find_student(roll_no)
    if student == None:
        print("Student not found.")
        return
    marks = student["marks"]
    average = average_marks(marks)

    print("\nName:", student["name"])
    print("Roll No:", student["roll_no"])
    print("Total Marks:", total_marks(marks))
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest_marks(marks))
    print("Lowest Marks:", lowest_marks(marks))
    print("Attendance:", student["attendance"], "%")

    print("\n========== SUBJECT REPORT ==========")

    for i in range(len(subjects)):
        print("\nSubject:", subjects[i])
        print("Marks:", marks[i])
        print("Grade:", grade(marks[i]))
        print("Grade Point:", grade_point(marks[i]))
        subject_feedback(subjects[i], marks[i])

    print("\n========== ATTENDANCE ==========")
    attendance_feedback(student["attendance"])

    print("\n========== OVERALL FEEDBACK ==========")
    overall_feedback(average)
    study_plan(average)

    print("\n========== WEAK SUBJECTS ==========")
    found = False

    for i in range(len(subjects)):
        if marks[i] < 60:
            print(subjects[i], "needs more attention.")
            found = True
    if found == False:
        print("No major weak subject found.")

# ================= UPDATE MARKS =================
def update_marks():
    print("\n========== UPDATE MARKS ==========")

    roll_no = input("Enter Roll No: ")
    student = find_student(roll_no)

    if student == None:
        print("Student not found.")
        return

    for i in range(len(subjects)):
        print(i + 1, ".", subjects[i], "-", student["marks"][i])

    choice = int(input("Enter subject number: "))

    if choice < 1 or choice > 4:
        print("Invalid choice.")
        return

    mark = int(input("Enter new marks: "))

    while mark < 0 or mark > 100:
        print("Marks should be between 0 and 100.")
        mark = int(input("Enter new marks: "))

    student["marks"][choice - 1] = mark
    save_all_students()

    print("Marks updated successfully.")

# ================= UPDATE ATTENDANCE =================

def update_attendance():
    print("\n========== UPDATE ATTENDANCE ==========")
    roll_no = input("Enter Roll No: ")
    student = find_student(roll_no)

    if student == None:
        print("Student not found.")
        return

    attendance = int(input("Enter new attendance: "))

    while attendance < 0 or attendance > 100:
        print("Attendance should be between 0 and 100.")
        attendance = int(input("Enter new attendance: "))
    student["attendance"] = attendance
    save_all_students()

    print("Attendance updated successfully.")

# ================= DELETE STUDENT =================
def delete_student():
    print("\n========== DELETE STUDENT ==========")

    roll_no = input("Enter Roll No: ")
    student = find_student(roll_no)
    if student == None:
        print("Student not found.")
        return
    print("Student:", student["name"])
    confirm = input("Delete this student? ----> (yes/no): ")
    if confirm.lower() == "yes":
        students.remove(student)
        save_all_students()
        print("Student deleted successfully.")
    else:
        print("Delete cancelled.")

# ================= CLASS REPORT =================

def class_report():
    print("\n========== CLASS PERFORMANCE ==========")

    if len(students) == 0:
        print("No student data available.")
        return

    total = 0
    highest_student = students[0]
    for student in students:
        average = average_marks(student["marks"])
        total = total + average

        if average > average_marks(highest_student["marks"]):
            highest_student = student

    class_average = total / len(students)

    print("Total Students:", len(students))
    print("Class Average:", round(class_average, 2))
    print("Highest Performer:", highest_student["name"])
    print(
        "Highest Average:",
        round(average_marks(highest_student["marks"]), 2))

# ================= SUBJECT PERFORMANCE =================

def subject_performance():
    print("\n========== SUBJECT PERFORMANCE ==========")

    if len(students) == 0:
        print("No student data available.")
        return

    for i in range(len(subjects)):
        total = 0
        highest = 0
        lowest = 100

        for student in students:
            mark = student["marks"][i]
            total = total + mark

            if mark > highest:
                highest = mark

            if mark < lowest:
                lowest = mark

        average = total / len(students)

        print("\n", subjects[i])
        print("Average:", round(average, 2))
        print("Highest:", highest)
        print("Lowest:", lowest)

# ================= PASS / FAIL =================

def pass_fail_report():
    print("\n========== PASS / FAIL REPORT ==========")

    passed = 0
    failed = 0

    for student in students:
        fail = False

        for mark in student["marks"]:
            if mark < 40:
                fail = True

        if fail:
            failed = failed + 1
        else:
            passed = passed + 1

    print("Passed Students:", passed)
    print("Failed Students:", failed)

# ================= RANK LIST =================

def rank_list():
    print("\n========== RANK LIST ==========")

    ranking = students.copy()

    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):

            avg1 = average_marks(ranking[i]["marks"])
            avg2 = average_marks(ranking[j]["marks"])

            if avg2 > avg1:
                temp = ranking[i]
                ranking[i] = ranking[j]
                ranking[j] = temp

    rank = 1

    for student in ranking:
        print(
            rank,
            ".",
            student["name"],
            "-",
            round(average_marks(student["marks"]), 2)
        )
        rank = rank + 1


# ================= ATTENDANCE REPORT =================

def attendance_report():
    print("\n========== ATTENDANCE REPORT ==========")

    for student in students:
        print(
            student["name"],
            "-",
            student["attendance"],
            "%"
        )

    print("\nStudents below 75%:")

    for student in students:
        if student["attendance"] < 75:
            print(student["name"])


# ================= TOP PERFORMERS =================

def top_performers():
    print("\n========== TOP PERFORMERS ==========")

    ranking = students.copy()

    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):

            if average_marks(
                ranking[j]["marks"]
            ) > average_marks(
                ranking[i]["marks"]
            ):

                temp = ranking[i]
                ranking[i] = ranking[j]
                ranking[j] = temp
    limit = 3

    if len(ranking) < 3:
        limit = len(ranking)

    for i in range(limit):
        print(
            i + 1,
            ".",
            ranking[i]["name"],
            "-",
            round(
                average_marks(ranking[i]["marks"]),2))
# ================= BACKUP =================

def backup_data():
    file = open("students_backup.txt", "w")

    for student in students:
        file.write(student["name"] + "|")
        file.write(student["roll_no"] + "|")
        for mark in student["marks"]:
            file.write(str(mark) + "|")
        file.write(str(student["attendance"]) + "\n")
    file.close()
    print("Backup created successfully.")

# ================= STUDENT MENU =================

def student_menu():
    while True:
        print("\n========== STUDENT MENU ==========")
        print("1. Add Student")
        print("2. Student Report")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Update Attendance")
        print("6. Delete Student")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_report()

        elif choice == "3":
            roll = input("Enter Roll No: ")
            student = find_student(roll)

            if student == None:
                print("Student not found.")
            else:
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Marks:", student["marks"])
                print("Attendance:", student["attendance"], "%")

        elif choice == "4":
            update_marks()

        elif choice == "5":
            update_attendance()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            break

        else:
            print("Invalid choice.")
# ================= REPORT MENU =================

def report_menu():
    while True:

        print("\n========== REPORT MENU ==========")
        print("1. Class Performance")
        print("2. Subject Performance")
        print("3. Pass / Fail Report")
        print("4. Rank List")
        print("5. Attendance Report")
        print("6. Top Performers")
        print("7. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            class_report()
        elif choice == "2":
            subject_performance()
        elif choice == "3":
            pass_fail_report()
        elif choice == "4":
            rank_list()
        elif choice == "5":
            attendance_report()
        elif choice == "6":
            top_performers()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


# ================= MAIN =================

def main():
    load_students()
    print("======================================")
    print(" SMART STUDENT PERFORMANCE ANALYZER")
    print("======================================")

    print(
        "Students loaded from file:",
        len(students)
    )
    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Student Management")
        print("2. Class Reports")
        print("3. Backup Data")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_menu()

        elif choice == "2":
            report_menu()

        elif choice == "3":
            backup_data()

        elif choice == "4":
            save_all_students()
            print("All data saved.")
            print("Thank you for using the Student Performance Analyzer.")
            break
        else:
            print("Invalid choice. Try again.")
main()
