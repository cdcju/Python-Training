from teachers import Teacher
class Students(Teacher):
    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks
s = Students()
s.setId("001")
s.setMarks(96)

print(" The marks obtained by {} is {} ".format(s.getId(), s.getMarks()))