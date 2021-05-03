class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        self.eat = 0
        self.trial = len(students)
        while self.trial > 0:
            self.trial -= 1
            self.student = students.pop(0)
            if self.student == sandwiches[0]:
                sandwiches.pop(0)
                self.trial = len(students)
            else:
                students.append(self.student)
                self.student = None 
        return len(students)          