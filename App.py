from students.StudentService import StudentService
from courses.CourseService import CourseService
from results.ResultService import ResultService
from gradereports.GradeReport import GradeReport

student_service = StudentService()
course_service = CourseService()
result_service = ResultService()
grade_report = GradeReport(course_service, result_service)

def menu():
    print("\n==== GPA CALCULATOR ====")
    print("1. Register Student")
    print("2. Register Course")
    print("3. Enter Course Result")
    print("4. Generate GPA Report")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Student Name: ")
        student_service.add_student(sid, name)

    elif choice == "2":
        code = input("Course Code: ")
        title = input("Course Title: ")
        credit = float(input("Course Credit: "))
        course_service.add_course(code, title, credit)

    elif choice == "3":
        sid = input("Student ID: ")
        code = input("Course Code: ")
        grade = input("Letter Grade (A-F): ")
        result_service.add_result(sid, code, grade)

    elif choice == "4":
        sid = input("Student ID: ")
        grade_report.generate_report(sid)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
