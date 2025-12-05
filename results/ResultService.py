class ResultService:
    def __init__(self):
        # results = {student_id: {course_code: letter_grade}}
        self.results = {}

    def add_result(self, sid, code, grade):
        if sid not in self.results:
            self.results[sid] = {}
        self.results[sid][code] = grade.upper()
        print("Result recorded successfully.")

    def get_results(self, sid):
        return self.results.get(sid, {})
