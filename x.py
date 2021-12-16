class tile():
    isAlive = False
    
    def draw():
        pass
    def update(self,surroundings):
        if self.isAlive:
            if surroundings <= 1:
                self.isAlive = False
            elif surroundings >= 4:
                self.isAlive = False
        else:
            if surroundings == 3:
                self.isAlive = True
class map:
    mappedTiles = None
    def __init__(self) -> None:
        pass
    def draw():
        pass
    def update():
        pass
        

        
     