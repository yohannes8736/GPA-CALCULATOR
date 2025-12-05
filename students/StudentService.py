class StudentService:
    def __init__(self):
        self.students = {}   # {student_id: {name}}

    def add_student(self, sid, name):
        self.students[sid] = {"name": name}
        print("Student registered successfully.")

    def get_student(self, sid):
        return self.students.get(sid)
