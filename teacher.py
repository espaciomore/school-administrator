from quiz import Quiz

import copy
import datetime

class Teacher:

	name = ""
	quizzes = []

	def __init__(self, name):
		self.name = name

	def assignQuiz(self, student, quizID):
		#if type(quiz) is not Quiz:
		#	raise "A Quiz object must be provided"
		quiz = copy.deepcopy(self.quizzes[quizID])
		quiz.date = datetime.datetime.now()
		student.quizzes = student.quizzes + [quiz]
		return(student)

	def createQuiz(self, klass, questions, solutions):
		quiz = Quiz(klass, questions, solutions)
		self.quizzes = self.quizzes + [quiz]