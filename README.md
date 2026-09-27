# STUDENT-PERFORMANCE-ANALZER
## Overview

Student Performance Analyzer is a Python-based console application designed to manage and analyze student academic performance.

The application stores student information in a text file and provides features for entering marks and attendance, generating individual student reports, updating records, searching students, creating class-level reports, ranking students, identifying weak subjects, and creating a backup of stored data.

## Features

- Add a new student
- Store student name and roll number
- Store marks for four subjects
- Store attendance percentage
- Validate marks and attendance between 0 and 100
- Search students using roll number
- Generate an individual student performance report
- Calculate total, average, highest, and lowest marks
- Assign grades and grade points
- Provide subject-wise feedback
- Provide attendance feedback
- Provide overall performance feedback
- Generate a study plan based on average marks
- Identify weak subjects
- Update student marks
- Update student attendance
- Delete student records
- Generate class performance report
- Generate subject performance report
- Generate pass/fail report
- Generate rank list
- Generate attendance report
- Display top three performers
- Create a backup file
- Store data permanently using text-file handling

## Technologies / Tools Used

- Python 3
- Python functions
- Lists and dictionaries
- Conditional statements
- Loops
- String handling
- File handling
- Exception handling
- Git
- GitHub

No external Python libraries are required.

## Project Files

```text
Student-Performance-Analyzer/
│
├── main.py
├── README.md
├── statement.md
├── students.txt
├── students_backup.txt
├── PROJECT_REPORT.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── screenshots/
    └── README.md
```
## How to Install and Run

### 1. Install Python

Install Python 3 on your computer.

### 2. Download or clone the repository

Open the project folder in VS Code, IDLE, PyCharm, or another Python editor.

### 3. Run the program

Open a terminal inside the project folder and run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Testing Instructions

The project includes sample student records in `students.txt`.

After running the program, test the following:

1. Open **Student Management**.
2. Use **Student Report** and enter a sample roll number such as `26BCE1134`.
3. Use **Search Student** to verify a student's stored information.
4. Use **Update Marks** and verify that the updated marks are saved.
5. Use **Update Attendance** and verify that the new attendance is saved.
6. Use **Delete Student** only on a test record if you want to demonstrate deletion.
7. Open **Class Reports**.
8. Test Class Performance.
9. Test Subject Performance.
10. Test Pass / Fail Report.
11. Test Rank List.
12. Test Attendance Report.
13. Test Top Performers.
14. Use **Backup Data** from the main menu and check that `students_backup.txt` is updated.

## Input Validation

The program checks that:

- Marks are between 0 and 100.
- Attendance is between 0 and 100.
- Duplicate roll numbers are not accepted.
- Invalid menu choices are rejected.

## Screenshots

Screenshots are optional but recommended by the submission requirements.

See `screenshots/README.md` for the exact screenshots to capture and what each screenshot should demonstrate.

## Sample Roll Numbers

The sample records use the following roll-number sequence:

- 26BCE1134
- 26BCE1135
- 26BCE1136
- 26BCE1137
- 26BCE1138
- 26BCE1139
- 26BCE1140
- 26BCE1141
- 26BCE1142

The marks and attendance values are sample project data.
