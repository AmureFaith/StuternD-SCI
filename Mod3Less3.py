class Group_leader:
         def __init__(self,fname,lname,student):
              self.student = student
              super().__init__(fname,lname)

         def Group_leader(self,fname,lname,student):
             List_students = []
             List_students.append(student)
             print(List_students)

         def remove_student(self,student):
             List_students = List_students[student]
             List_students.pop(student)

         def fullname_student(self):
            return "{} {}".format(self.fname,self.lname)
         def stud1()
  
