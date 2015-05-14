'''
Created on Apr 18, 2015

@author: Derek Dik
'''

class Experience(object):
    '''
    Experience models the memory system of an NPC. Each NPC character or creature will contain a single experience object.
    The Experience class contains methods to recall information regarding the place, time, and existance of certain objects.
    '''
    time = 0    
    myMemories = []
    NearbyEntities = []
    recalledEntities = []
    location = []
    myObstacles = [] 
    x = 0
    y = 0
    _water = 0
    _food = 0
    _loneliness = 0
    def __init__(self):
        '''
        Constructor
        '''
    
    def perceive(self, staticObjects, dynamicObjects, x, y, water, food, loneliness):
        # Tick the time by one
        self.time += 1    
        self.myObstacles = staticObjects
        self.NearbyEntities = dynamicObjects
        for entity in dynamicObjects:
            if self.recalledEntities.count(entity) == 0:
                self.recalledEntities.append(entity)
                print("Spotted new entity and committed to long term memory: " + entity.type())
        self.x = x
        self.y = y
        self._water = water
        self._food = food
        self._loneliness = loneliness
        
    def get_water(self):
        return self._water
    
    def get_food(self):
        return self._food
    def get_loneliness(self):
        return self._loneliness
    
    def getSurroundings(self):
        '''
        Returns [myObstacles, nearbyEntities]
        '''
        return [self.myObstacles, self.nearbyEntities]
    
    def get_position(self):
        return [self.x, self.y]
    def changeLocation(self, location):
        self.commitToLongTerm()
        self.location = location
        
    def commitToLongTerm(self):
        memory = Experience.Memory("A place", self.location, self.NearbyEntities, self.time)
        self.myMemories.append(memory)
        self.NearbyEntities = []
        print("Commited a memory to long term memory")
        
    def getMemory(self, location):
        '''
        Parameters: location
        Precondition: location is a valid location in [x, y] form
        Return: [locationDesc, timeElapsed, entities], 0 (if memory is not found)
        Postcondition: locationDesc is a string, timeElapsed is an integer, entities is a list of DynamicObjects
        '''
        for memory in reversed(self.myMemories):
            if memory.location == location:
                return [memory.locationDesc, self.time - memory.time, memory.NearbyEntities]
       
        # Memory not found
        return 0
    
    def getLocation(self, locationDesc):
        '''
        Parameters: locationDesc
        Precondition: location is a valid location in [x, y] form
        Return: [x, y], 0 (if memory is not found)
        Postcondition: location is a valid location in [x, y] form
        '''
        for memory in reversed(self.myMemories):
            if memory.locationDesc == locationDesc:
                return memory.location
       
        # Memory not found
        return 0
    
    def getLastSeenLocation(self, entity):
        '''
        Parameters: entity
        Precondition: entity is a valid dynamic object
        Return: [x, y], 0 (if memory is not found), 1 (if the entity is in the room)
        Postcondition: location is a valid location in [x, y] form
        '''
        if self.NearbyEntities.count(entity) > 0:
            # The entity is right here!
            return 1
        
        for memory in reversed(self.myMemories):
            if memory.NearbyEntities.count(entity) > 0: 
                return memory.location
       
        # Memory not found
        return 0
    
    def sees_player(self):
        for entity in self.NearbyEntities:
            if entity.type() == "Player":
                return True
        return False
    
    def get_player_location(self):
        for entity in self.NearbyEntities:
            if entity.type() == "Player":
                return [entity.getX(), entity.getY()]
        return [0, 0]
    
    class Memory(object):
        location = []
        locationDesc = ""
        NearbyEntities = []
        time = 0
        
        def __init__(self, description, location, dynamicObjects, time):
            '''
            Constructor
            '''
            self.location = location
            self.NearbyEntities = dynamicObjects
            self.locationDesc = description
            self.time = time
            