from klass import Klass
from teacher import Teacher
from student import Student
from quiz import Quiz

import datetime
import unittest

class Tests(unittest.TestCase):
	
	klasses = []
	teachers = []
	students = []

	@classmethod
	def setUpClass(self):
		self.klasses = [Klass(3),Klass(2)]
		self.teachers = [Teacher("John Due"), Teacher("Mary Anne")]
		self.students = [Student("Tom Hardey"), Student("Jane Watson"), Student("Larry Bird")]
		# assign teachers to classes
		self.klasses[0].assignTeacher(self.teachers[0])
		self.klasses[1].assignTeacher(self.teachers[1])
		# add students to classes
		self.klasses[0].addStudent(self.students[0])
		self.klasses[0].addStudent(self.students[1])
		self.klasses[1].addStudent(self.students[1])
		self.klasses[1].addStudent(self.students[2])
		# let teachers create quiz
		self.teachers[0].createQuiz(self.klasses[0], ["W","X","Y","Z"], ["A","B","C","D"])
		# let teachers assign the quiz to students
		self.teachers[0].assignQuiz(self.students[0], 0)
		self.teachers[0].assignQuiz(self.students[1], 0)
		self.teachers[0].assignQuiz(self.students[2], 0)
		# let students submit their answers
		self.students[0].submitAnswers(0, ["A","B","C","D"])
		self.students[1].submitAnswers(0, ["A","B","B","D"])
		self.students[2].submitAnswers(0, ["A","B","C"])
		pass

	def test_that_student_can_join_class_of_particular_teacher(self):
		# the student joins a particular class
		self.assertIn(self.teachers[0], self.klasses[0].teachers)
		self.assertIn(self.students[0], self.klasses[0].students)

	def test_that_teacher_can_create_quiz(self):
		# the teacher creates a quiz with many questions (each question is multiple choice)
		self.assertEqual(len(self.teachers[0].quizzes), 1)
		self.assertEqual(len(self.teachers[0].quizzes[0].questions), 4)

	def test_that_teacher_can_assign_quiz_to_student(self):
		# the teacher assigns a quiz to a student
		self.assertEqual(len(self.students[0].quizzes), 1)

	def test_that_student_can_make_partial_submission(self):
		# the student submits an incomplete quizz
		self.assertNotEqual(len(self.students[2].quizzes[0].questions), len(self.students[2].quizzes[0].answers))

	def test_that_quizz_can_be_graded(self):
		# the quizz is graded
		self.assertEqual(self.students[0].quizzes[0].getGrade(), "A")
		self.assertEqual(self.students[1].quizzes[0].getGrade(), "C")
		self.assertEqual(self.students[2].quizzes[0].getGrade(), "C")

	def test_that_student_gpa_can_be_calculated(self):
		# the student's gpa is calculated
		now = datetime.datetime.now()
		self.assertEqual(self.students[0].getGPA(now - datetime.timedelta(days=30*3), now), 4.0)

if __name__ == "__main__":
	unittest.main()