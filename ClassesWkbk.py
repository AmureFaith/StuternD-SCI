class Employee:

  def set_name(self, new_name):
    self.name = new_name
  
  def set_salary(self, new_salary):
    self.salary = new_salary

# Create an object emp of class Employee  
emp = Employee()

#Try printing emp.salary before and after calling set_salary().
# Before setting salary
#print(emp.salary)

# Set the salary of emp to 50000.
emp.set_salary(50000)
# After setting salary
print(emp.salary)
