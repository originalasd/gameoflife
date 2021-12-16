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
    def toggle(self):
        self.isAlive = not self.isAlive 
            

class map:
    mappedTiles = None
    def __init__(self) -> None:
        self.mappedTiles = []
        for column in range(20):
            self.mappedTiles.append([])
            for rows in range(20):
                self.mappedTiles[column].append(tile())
    def draw():
        pass
    def update():
        pass
        

        
     