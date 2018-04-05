from teacher import Teacher
from student import Student

class Klass:

	students = []
	teachers = []
	units = 0

	def __init__(self, weight):
		if type(weight) is not int or weight < 0:
			raise "Units must be a whole number"
		self.units = weight

	def assignTeacher(self, teacherX):
		#if type(teacherX) is not Teacher:
		#	raise "Object must be a Teacher"
		if teacherX not in self.teachers:
			self.teachers = self.teachers + [teacherX]

	def addStudent(self, studentX):
		#if type(studentX) is not Student:
		#	raise "Object must be a Teacher"
		if studentX not in self.students:
			self.students = self.students + [studentX]

