class DasBoot:
    def __init__(self, dmg, ammo, hp, xcoord, ycoord, picpath="pil.png", picpath_fire = "fire_pil.png"):

        #~ "////////////////////"
        #~ "Game STATS"
        #~ "////////////////////"


        self.d = dmg
        self.h = hp
        self.ammostash = ammo

        self.spd = 5
        #~ "Removed speed, since irrelevant without a vector"
        #~ "See new entry (dx,dy) under 'Physics'"
        #~
        #~ "////////////////////"
        #~ "Physics"
        #~ "////////////////////"
        #~
        #~ "Mass"
        self.mass = 1.0

        #~ "Volume: square(s), cube(s) that define the volume the ship occupies"
        self.bounds = []

        #~ "coords"
        self.x = xcoord
        self.y = ycoord
        #~ "velocity"
        self.dx = 0.0
        self.dy = 0.0
        #~ "direction of bow"
        self.ix = 0.0
        self.iy = 1.0

        #~
        #~ "////////////////////"
        #~ "Modules"
        #~ "////////////////////"
        
        #~ What we want the boat to do
        self.order=[]
        self.FIRE_ACTIVE = 0

        #~ "propulsion: sails, oars, propeller"
        self.propulsion = []
        self.afterburners = []

        #~ "Cannons!"
        self.cannons = []
        #~
        #~ "////////////////////"
        #~ "Graphics"
        #~ "////////////////////"
        #~
        self.picpath = picpath
        self.picpath_fire = picpath_fire
        
        self.drawx = xcoord
        self.drawy = ycoord

        # Target position
        self.targetheadingx = xcoord
        self.targetheadingy = ycoord

    @property
    def propulsion(self):
        return self._propulsion

    @propulsion.setter
    def propulsion(self, value):
        self._propulsion = value
