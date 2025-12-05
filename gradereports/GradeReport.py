class GradeReport:

    grade_points = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self, course_service, result_service):
        self.course_service = course_service
        self.result_service = result_service

    def generate_report(self, sid):
        results = self.result_service.get_results(sid)

        if not results:
            print("No results found for this student.")
            return

        total_credits = 0
        total_grade_points = 0

        print("\n==== STUDENT GPA REPORT ====")

        for code, grade in results.items():
            course = self.course_service.get_course(code)
            if not course:
                print(f"Course {code} not found! Skipping...")
                continue

            credit = course["credit"]
            grade_point = self.grade_points.get(grade, 0)

            total_credits += credit
            total_grade_points += grade_point * credit

            print(f"{code} - {course['title']}: Grade {grade}, Credit {credit}")

        if total_credits == 0:
            print("No valid courses found.")
            return

        gpa = total_grade_points / total_credits
        print(f"\nTotal Credits: {total_credits}")
        print(f"GPA: {gpa:.2f}")
