class Question:

	description = ""
	typeOf = "Multi"
	options = []

	def __init__(self, desc, opts):
		if type(opts) is not list:
			raise "Options must be a list object"
		self.description = desc
		self.options = opts