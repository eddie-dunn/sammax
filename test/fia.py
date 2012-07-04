
class fia:
	"For the Glory"
	def __init__(self):
		self.i = 0
	
	def f(self):
		return "boo"
	def a_func(self):
		self.i = self.i + 1
		return self.i
		
a = fia()
print a.f()

print a.a_func()
