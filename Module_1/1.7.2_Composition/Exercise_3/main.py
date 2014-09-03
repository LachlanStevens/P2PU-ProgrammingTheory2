from course import *

def main():

	firstCourse = Course(1)
	print
	print "========="
	print "|Courses|"
	print "========="
	print
	firstCourse.addCourse("Maths")
	firstCourse.listCourses()
	print
	firstCourse.removeCourse(2)
	firstCourse.listCourses()
	print
	print "=============="
	print "|Conversation|"
	print "=============="
	print
	firstCourse.student.talk("Hi.")
	firstCourse.teacher.talk("Get back to class!")
	firstCourse.student.move("Class")
	print
	print "=========="
	print "|Students|"
	print "=========="
	print
	firstCourse.student.add("Scott V. Bonilla")
	firstCourse.student.list()
	print
	firstCourse.student.remove(4)
	firstCourse.student.list()
	print
	print "=========="
	print "|Teachers|"
	print "=========="
	print
	firstCourse.teacher.add("Roger D. Boddie")
	firstCourse.teacher.list()
	print
	firstCourse.teacher.remove(3)
	firstCourse.teacher.list()
	print

if(__name__ == "__main__"):
	main()