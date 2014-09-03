class Departments:

  departmentArray = [
    "Service",
    "Development",
    "Admin",
    "Finance"
  ]

  def addDepartment(self,departmentToAdd):
    self.departmentArray.append(departmentToAdd)

  def removeDepartment(self,departmentIndex):
    del self.departmentArray[departmentIndex-1]

  def listDepartments(self):
    i = 1
    for department in self.departmentArray:
      print "#%d: %s" % (i, department)
      i += 1

class Employees:

  employeeArray = [
    "Ernest V. Calhoun",
    "Carmen R. Martinez",
    "Grace C. Beltran",
    "Michael S. Heller"
  ]

  def addEmployee(self,employeeName):
    self.employeeArray.append(employeeName)

  def removeEmployee(self,employeeIndex):
    del self.employeeArray[employeeIndex-1]

  def listEmployees(self):
    i = 1
    for employee in self.employeeArray:
      print "#%d: %s" % (i,employee)
      i += 1

class Company:

  id = 0
  departments = Departments()
  employees = Employees()

  def __init__(self, id):

    self.id = id