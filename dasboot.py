class DasBoot:
	def __init__(self, dmg, hp, xcoord, ycoord):
		
		"////////////////////"
		"Game STATS"
		"////////////////////"
		
		self.d = dmg
		self.h = hp
		"Removed speed, since irrelevant without a vector"
		"See new entry (dx,dy) under 'Physics'"
		
		
		
		"////////////////////"
		"Physics"
		"////////////////////"
		
		"Mass"
		self.mass = 1.0
		
		"Volume: square(s), cube(s) that define the volume the ship occupies"
		self.bounds = []
		
		"coords"
		self.x = xcoord
		self.y = ycoord
		"velocity"
		self.dx = 0.0
		self.dy = 0.0
		"direction of bow"
		self.ix = 0.0
		self.iy = 1.0
		
		
		
		"////////////////////"
		"Modules"
		"////////////////////"
		
		"propulsion: sails, oars, propeller"
		self.propulsion = []
		
		"Cannons!"
		self.cannons = []
		
		"afterburnes?"
		self.afterburners = []
		
		"ammunition?"
		self.ammostash = []
