import itertools


class Sentence():

	def evaluate(self, model):
		#Evaluates the logical sentence
		raise Exception("nothing to evaluate")

	def formula(self):
		#Returns string formula for logical sentence
		return ""

	def symbols(self):
		#Returns a set of all symbols in the logical sentence #Symbolo son las partes (Q,R,P)
		return set()

	@classmethod
	def validate(cls, sentence):
		if not isinstance(cls,sentence):
			raise TypeError("must be a logical sentence")

	@classmethod
	def parenthesize(cls, s):
		#Parenthesizes an expression if not already parenthesized
		def balanced(s):
			#checks if a string has balanced parentheses
			count=0
			for c in s:
				if c== "(":
					count+=1
				elif c== ")":
					if count <=0:
						return False
					count-= 1
			return count == 0
		if not len(s) or s.isalpha() or (
			s[0]=="(" and s[-1]==")" and balanced(s[1:-1])
		):
			return s
		else:
			return f"({s})"


class Symbol(Sentence):

	def __init__(self, name):
		self.name= name 

		def __eq__(self, other):
			return isinstance(other, Symbol) and self.name==other.name

		def __hash__(self):
			return hash(("symbol", self.name))

		def __repr__(self):
			return self.name

		def evaluate(self, model):
			try:
				return bool(model[self.name])
			except KeyError:
				raise EvaluationException(f"variable{self.name} not in model")

		def formula(self):
			return self.name

		def symbols(self):
			return {self.name}


class Not(Sentence):
	def __init__(self, operand):
		Sentence.validate(operand)
		self.operand=operand

	def __eq__(self, other):
		return isinstance(other, Not) and self.operand==other.operand

	def __hash__(self):
		return hash(("not", hash(self.operand)))

	def __repr__(self):
		return f"Not({self.operand})"

	def evaluate(self, model):
		return not self.operand.evaluate(model)

	def formula(self):
		return "¬"+Sentence.parenthesize(self.operand.formula())

	def symbols(self):
		return self.operand.symbols()


class And(Sentence):
	def __init__(self, *conjuncts):
		for conjunct in conjuncts:
			Sentence.validate(conjunct)
		self.conjuncts = list(conjuncts)

	def __eq__(self, other):
		return isinstance(other, And) and self.conjuncts==other.conjuncts

	def __hash__(self):
		return hash(
			("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
			)

		def __repr__(self):
			conjunctions=", ".join(
				[str(conjunct) for conjunct in self.conjuncts]
				)
			return f"And({conjunctions})"

		def add(self, conjunct):
			Sentence.validate(conjunct)
			self.conjuncts.append(conjunct)