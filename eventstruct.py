"""
Documentation

"""


class EventStruct:
    """
    Doc string...
    
    """
    def __init__(self, target, key, values=0, active=0):
        """
        Constructor. target and key parameters are not optional

        @param target: Object that event relates to
        @type target: object

        @param key: Event type, i.e. "_move_to_coord_", "_fire_weapon_" etc.
        @type key: string

        @param values: Boat hitpoints
        @type values: double[] - number of input depends on 'key'
        """
        
        #Initialized variables
        self.target = target
        self.key = key
        self.values = values
        self.active = active
    
    def getTarget(self):
        """ return 'target' """
        return self.target
        
    def getKey(self):
        """ return 'key' """
        return self.key
        
    def getValues(self):
        """ return 'values' """
        return self.values

    def isActive(self):
		return self.active

    def setActive(self,A):
		self.active = A


def clean_event_array(A):
	#~ 	Static function
	SIZE = len(A)
	i = 0
	#~ Remove inactive events
	while( i < SIZE):
		if(A[i].isActive() == -1):
			del A[i]
			i -= 1
			SIZE -= 1
		i += 1
	
	#~ Remove doubles
	i = 0
	k = 1
	SIZE = len(A)
	while i < SIZE:
		while k < SIZE:
			if A[i].getKey() == A[k].getKey():
				del A[i]
				i -= 1
				k = SIZE
				SIZE -= 1
			k += 1
		i += 1
		k = i + 1
