from company import *

def main():

	company1 = Company(1)

	company1.departments.addDepartment("Computing")
	company1.departments.listDepartments()
	print
	company1.departments.removeDepartment(3)
	company1.departments.listDepartments()
	print
	company1.employees.addEmployee("Don S. Phillips")
	company1.employees.listEmployees()
	print
	company1.employees.removeEmployee(2)
	company1.employees.listEmployees()

if(__name__ == "__main__"):
	main()