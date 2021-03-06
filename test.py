from klass import Klass
from teacher import Teacher
from student import Student
from quiz import Quiz
from question import Question

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
		question1 = Question("What is a man?", ["An animal", "A bird", "An alien", "A God"])
		question2 = Question("When did Jesus die?", ["02/25/0233", "00/00/0000", "12/24/0000", "04/04/0000"])
		question3 = Question("What is Santa Claus?", ["A legend", "A hero", "An man", "An icon"])
		question4 = Question("What is a star?", ["Earth", "Venus", "Moon", "Sun"])
		solutions = ["A","B","C","D"]
		self.teachers[0].createQuiz(self.klasses[0], [question1, question2, question3, question4], solutions)
		# let teachers assign the quiz to students
		self.teachers[0].assignQuiz(self.students[0], 0)
		self.teachers[0].assignQuiz(self.students[1], 0)
		self.teachers[0].assignQuiz(self.students[2], 0)
		# let students submit their answers
		self.students[0].submitAnswers(0, ["A","B","C","D"])
		self.students[1].submitAnswers(0, ["A","B","B","A"])
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
		self.assertEqual(self.students[1].quizzes[0].getGrade(), "F")
		self.assertEqual(self.students[2].quizzes[0].getGrade(), "C")

	def test_that_student_gpa_can_be_calculated(self):
		# the student's gpa is calculated
		now = datetime.datetime.now()
		startDate = now - datetime.timedelta(days=30*3)
		self.assertEqual(self.students[0].getGPA(startDate, now), 4.0)
		self.assertEqual(self.students[1].getGPA(startDate, now), 0.0)
		self.assertEqual(self.students[2].getGPA(startDate, now), 2.0)

if __name__ == "__main__":
	unittest.main()
