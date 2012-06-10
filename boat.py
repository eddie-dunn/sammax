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

    def __init__(self, x=0, y=0, hp=5, picpath="boat.jpg"):
    # Disabling pylint complaints on too short variable names
    # pylint: disable=C0103
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

        self._hp = hp
        self._ammo = 5
        self._x = x
        self._y = y

        # "Direction of bow"
        self._xdir = 0.0
        self._ydir = 1.0

        self._picpath = picpath

    @property
    def drawx(self):
        """To be deprecated. Thomas currently uses this for unknown reasons."""
        return self._x

    @drawx.setter
    def drawx(self, value):
        """To be deprecated. Thomas currently uses this for unknown reasons."""
        self._x = value

    @property
    def drawy(self):
        """To be deprecated. Thomas currently uses this for unknown reasons."""
        return self._x

    @drawy.setter
    def drawy(self, value):
        """To be deprecated. Thomas currently uses this for unknown reasons."""
        self._y = value
