class StudentService:
    def __init__(self):
        self.students = {}   # {student_id: {firstname,lastname}}

    def add_student(self, sid, firstname,lastname):
        self.students[sid] = {"firstname": firstname,"lastname": lastname}
        print("Student registered successfully.")

    def get_student(self, sid):
        return self.students.get(sid)
