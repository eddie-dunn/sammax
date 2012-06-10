"""
This is how you write a good python module.

Install pylint and pep8:
sudo easy_install pylint pep8
sudo apt-get install pylint pep8

Then run this on your files to make sure you follow Python conventions
and to remove "lint" from your code.
"""


class Boat:
    """
    A simple boat class to be used in the boatgame. Intended to be
    subclassed and extended for different boats.
    """

    def __init__(self, x=0, y=0, name="n1", picpath="boat.jpg"):
    # pylint: disable=C0103
    # Disable pylint complaints about too short variable names
        """
        Constructor. All parameters are optional.

        @param x: Boat x position
        @type x: int

        @param y: Boat y position
        @type y: int

        @param hp: Boat hitpoints
        @type hp: int

        @param picpath: Path to this boat's picture
        @type picpath: string

        """

        # Initialized variables
        self.x = x
        self.y = y
        self._picpath = picpath
        self.name = name

        # Variables with default values
        self.hp = 10
        self.ammo = 5

        # "Direction of bow"
        self._xdir = 0.0
        self._ydir = 1.0

    @property
    def image_path(self):
        """Return filepath of boat's image sprite."""
        return self._picpath

    @property
    def direction(self):
        """A the direction the boat is headed in."""
        return (self._xdir, self._ydir)

    def move(self, direction):
        if 'left' in direction:
            self.x -= 1
        elif 'right' in direction:
            self.x += 1
        elif 'up' in direction :
            self.y += 1
        elif 'down' in direction:
            self.y -= 1
