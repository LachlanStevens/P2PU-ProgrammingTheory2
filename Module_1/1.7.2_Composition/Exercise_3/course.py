from person import *

class Teacher():

	teacherArray = [
		"Glenn S. Perryman",
		"Marlene B. Greer",
		"John M. Beaver",
		"Debra J. Tammaro",
		"Nancy M. Whyte"
	]

	def add(self,name):
		self.teacherArray.append(name)

	def remove(self,index):
		del self.teacherArray[index-1]

	def list(self):
		i = 1
		for teacher in self.teacherArray:
			print "#%d: %s" % (i, teacher)
			i += 1

	def talk(self,text):
		print "Teacher: %s" % (text)

	def move(self,location):
		print "Teacher moved to: %s" % (location)

class Student():

	studentArray = [
		"Billy M. Marrero",
		"Jeffrey M. Hall",
		"Ricardo S. Hunter",
		"Mary J. Zielinski",
		"James E. Reams"
	]

	def add(self,name):
		self.studentArray.append(name)

	def remove(self,index):
		del self.studentArray[index-1]

	def list(self):
		i = 1
		for student in self.studentArray:
			print "#%d: %s" % (i, student)
			i += 1

	def talk(self,text):
		print "Student: %s" % (text)

	def move(self,location):
		print "Student moved to: %s" % (location)

class Course:

	id = 0
	teacher = Teacher()
	student = Student()

	courseArray = [
		"Computing Science 1",
		"Computing Science 2",
		"Visual Communications",
		"Computing Analysis",
		"Quantum Computing"
	]

	def addCourse(self,inputCourse):
		self.courseArray.append(inputCourse)

	def removeCourse(self,courseIndex):
		del self.courseArray[courseIndex-1]

	def listCourses(self):
		i = 1
		for course in self.courseArray:
			print "#%d: %s" % (i, course)
			i += 1

	def __init__(self, id):
		self.id = id