
class boat:
	"What is a boat?"
	def __init__(self):
		"Mass"
		self.mass = 1.0
		
		"Volume: square(s), cube(s) that define the volume the ship occupies"
		self.bounds = []
		
		"coords"
		self.x = 0.0
		self.y = 0.0
		"velocity"
		self.dx = 0.0
		self.dy = 0.0
		"direction of bow"
		self.ix = 0.0
		self.iy = 1.0
		
		"propulsion: sails, oars, propeller"
		self.propulsion = []
		
		"Cannons!"
		self.cannons = []
		
		"afterburnes?"
		self.afterburners = []
		
		"ammunition?"
		self.ammostash = []
		
		
		
