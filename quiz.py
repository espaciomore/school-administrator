import datetime

class Quiz:
	
	klass = None
	questions = []
	solutions = []
	answers = []
	date = None

	def __init__(self, klassObject, questions, solutions):
		if len(questions) != len(solutions):
			raise "Each question should have a solution"
		if not questions:
			raise "Must provide at least one question"
		self.questions = questions
		self.solutions = solutions
		self.klass = klassObject

	def getGrade(self):
		points = 0
		for i, answer in enumerate(self.answers):
			if i<len(self.solutions) and self.solutions[i] == answer:
				points += 1
		grade = float(points) / float(len(self.questions))
		if grade >= 0.9:
			return("A")
		if grade >= 0.8:
			return("B")
		if grade >= 0.7:
			return("C")
		if grade >= 0.6:
			return("D")
		
		return("F")