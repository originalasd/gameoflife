


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
    def update(self):
        pastMapped = self.mappedTiles
        surroundRow = []
        surroundCol = []
        """
        in the list row we need -1 and +1 to the same list, in the colummn list -1 and +1 list 
        """
        for column in range(20):
            if column == 0:
                surroundCol = [0,1]
            elif column == 19:
                surroundCol = [18,19]
            else:
                surroundCol = [column-1,column,column+1]
            for rows in range(20):
                if rows == 0:
                    surroundRow = [0,1]
                elif rows == 19:
                    surroundRow = [18,19]
                else:
                    surroundRow = [rows-1,rows,rows+1]
                """
                look at 8 postions,located in surrondrow and column, in pastmapped
                """
                for 
        
     