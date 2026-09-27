# Project Report — STUDENT PERFORMANCE ANALYZER

## 1. Introduction

The Student Performance Analyzer is a Python console application developed to manage and analyze student academic records.

The project demonstrates fundamental programming concepts such as variables, lists, dictionaries, functions, loops, conditional statements, input validation, searching, sorting logic, and file handling.

## 2. Objectives

The main objectives are:

1. Store student academic records.
2. Calculate important performance statistics.
3. Generate individual student reports.
4. Analyze performance at class and subject levels.
5. Monitor student attendance.
6. Identify weak subjects and provide basic feedback.
7. Maintain records using permanent text-file storage.
8. Provide a backup facility.

## 3. Subjects

The current program analyzes four subjects:

- MAT1003
- CSE1021
- ENG1004
- CHY1001

## 4. System Design

The application follows a menu-driven structure.

### Main Menu

```text
1. Student Management
2. Class Reports
3. Backup Data
4. Exit
```

### Student Management

The student-management section provides:

- Add Student
- Student Report
- Search Student
- Update Marks
- Update Attendance
- Delete Student

### Report Menu

The report section provides:

- Class Performance
- Subject Performance
- Pass / Fail Report
- Rank List
- Attendance Report
- Top Performers

## 5. Data Structure

Each student is stored as a dictionary:

```python
{
    "name": "Piyush",
    "roll_no": "26BCE1134",
    "marks": [85, 78, 91, 74],
    "attendance": 88
}
```

All student dictionaries are stored in a list.

## 6. File Handling

The project uses two text files:

### students.txt

This is the main data file. Each record contains:

```text
name|roll_no|mark1|mark2|mark3|mark4|attendance
```

### students_backup.txt

This file stores a backup copy of the student records when the Backup Data option is selected.

## 7. Major Calculations

The application calculates:

- Total marks
- Average marks
- Highest marks
- Lowest marks
- Grade
- Grade point
- Class average
- Subject average
- Subject highest mark
- Subject lowest mark

## 8. Grade System

The current program uses the following grade ranges:

| Marks | Grade | Grade Point |
|---|---|---:|
| 90–100 | S | 10 |
| 80–89 | A | 9 |
| 70–79 | B | 8 |
| 60–69 | C | 7 |
| 50–59 | D | 6 |
| 40–49 | E | 5 |
| 0–39 | F | 0 |

## 9. Attendance Analysis

The application checks attendance against a 75% threshold.

- Below 75%: attendance warning
- 75%–84%: acceptable attendance
- 85% and above: excellent attendance

## 10. Performance Feedback

The program provides feedback based on subject and overall average marks.

It can:

- Identify subjects needing improvement
- Suggest regular revision
- Suggest additional question practice
- Suggest advanced-question practice for higher-performing students
- Generate a basic study plan

## 11. Ranking

The rank-list feature creates a copy of the student list and orders students by their average marks using comparison and swapping logic.

The Top Performers feature displays up to the top three students.

## 12. Validation

The application validates:

- Marks from 0 to 100
- Attendance from 0 to 100
- Duplicate roll numbers
- Invalid menu choices
- Student existence before update/delete/report operations

## 13. Testing

The application should be tested using the sample records included in `students.txt`.

Recommended tests:

| Test | Expected Result |
|---|---|
| Add valid student | Student is added and saved |
| Add duplicate roll number | Duplicate is rejected |
| Enter marks below 0 or above 100 | Input is requested again |
| Enter attendance outside 0–100 | Input is requested again |
| Search existing roll number | Student details are displayed |
| Search unknown roll number | Student not found message |
| Update marks | New marks are saved |
| Update attendance | New attendance is saved |
| Delete student | Student is removed after confirmation |
| Generate report | Individual performance is displayed |
| Generate class report | Class statistics are displayed |
| Generate rank list | Students are displayed by average |
| Create backup | Backup file is created |

## 14. Limitations

The current version is intentionally a beginner-friendly console application.

Current limitations include:

- Text-file storage instead of a database
- No graphical user interface
- No user authentication
- No PDF/Excel export
- No online/cloud storage
- Four subjects are fixed in the source code

## 15. Future Enhancements

Future versions could include:

- GUI using Tkinter
- Database using SQLite or MySQL
- Web application
- Login system
- Charts and dashboards
- PDF/Excel report generation
- CGPA calculation based on subject credits
- Multiple semesters
- Faculty/admin accounts
- Automated email/report features

## 16. Conclusion

The Student Performance Analyzer demonstrates how Python programming concepts can be combined to build a practical academic record-management application.

The project provides student management, performance analysis, attendance monitoring, class reports, ranking, feedback, and backup functionality while maintaining data through simple text files.
