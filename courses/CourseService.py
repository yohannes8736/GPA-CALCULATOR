class CourseService:
    def __init__(self):
        self.courses = {}  # {code: {title, credit}}

    def add_course(self, code, title, credit):
        self.courses[code] = {
            "title": title,
            "credit": credit
        }
        print("Course added successfully.")

    def get_course(self, code):
        return self.courses.get(code)
