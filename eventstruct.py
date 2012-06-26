"""
Documentation

"""


class EventStruct:
    """
    Doc string...
    
    """
    def __init__(self, target, key, values=0):
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
    
    def getTarget(self):
        """ return 'target' """
        return self.target
        
    def getKey(self):
        """ return 'key' """
        return self.key
        
    def getValues(self):
        """ return 'values' """
        return self.values
