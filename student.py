class Student:

	name = ""
	quizzes = []

	def __init__(self, name):
		self.name = name

	def submitAnswers(self, quizID, answers):
		self.quizzes[quizID].answers = answers
		return(self.quizzes[quizID])

	def getGPA(self, startDate, endDate):
		points = 0
		totalunits = 0
		for quiz in self.quizzes:
			grade = quiz.getGrade()
			units = quiz.klass.units
			totalunits += units
			if grade == "A":
				points += 4*units
			if grade == "B":
				points += 3*units
			if grade == "C":
				points += 2*units
			if grade == "D":
				points += 1*units
			if grade == "F":
				points += 0*units
		return(float(points)/float(totalunits))