class School:
    def __init__(self):
        self._roster = {}
    def add_student(self, name, grade):
        self._roster[grade] = self._roster.get(grade, []) + [name]
        self._roster[grade].sort()
    def roster(self):
        respuesta = []
        for estudiante in [self._roster[key] for key in sorted(self._roster.keys())]:
            respuesta = respuesta + estudiante
        return respuesta 
    def grade(self, grade_numero):
        return self._roster.get(grade_numero, [])
