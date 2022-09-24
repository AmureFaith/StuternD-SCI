class Employee:
 # Define a class attribute
 MIN_SALARY = 30000 #<--- no self.
 def __init__(self, name, salary):
  self.name = name
  # Use class name to access class attribute
  if salary >= Employee.MIN_SALARY:
   self.salary = salary
  else:
   self.salary = Employee.MIN_SALARY
emp1 = Employee("TBD", 40000)
print(emp1.MIN_SALARY)

from datetime import datetime
current_time = datetime.now()
print(current_time)

