



class ResourceHandler(object):
    """Class to hold and organize input data"""

    def __init__(self, lookupTable):
        """Initiate new object; lookUpTable - string with path to lookup table"""
        self.pathLookupTable = lookupTable
        self.loadLookupTable()
        self._DATA = dict()


    def get(self,key):
        """Retrieve data corresponding to key"""
        if key in self._DATA :
            return self._DATA.get(key)
        elif key in self._lookupTable :
            return self.loadData(key)
        else :
            return None

    def loadLookupTable(self):
        """Load/reload lookup table to memory"""
        self._lookupTable = dict()
        with open(self.pathLookupTable) as f:
            for line in f:
                # print line,
                T = line.partition(" = ")
                self._lookupTable[T[0]] = T[2]
        pass


    def loadData(self,key):
        """Load data to memory, returns pointer to data"""
        # Not implemented yet
        print "LOADING: " + self._lookupTable[key] + "\n"
        return None


    def releaseData(self):
        """Return resource to system"""
        # Not implemented
        pass


R = ResourceHandler("resource.txt")
R.get("IMAGE_1")
R.releaseData()