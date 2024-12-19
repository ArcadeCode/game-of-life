import random
from time import sleep
from args import getargs

class GameBoard :
    def __init__(self, size: int):
        self._size = size
        self._iteration = 0
        self.gameboard = [[0 for ii in range(size)] for i in range(size)]

    def _isExist(self, x: int, y: int) -> bool:
        if x < 0 or y < 0 : return False
        if x > self._size or y > self._size : return False
        try:
            _ = self.gameboard[x][y]
            return True  # L'élément existe
        except IndexError:
            return False  # L'accès a déclenché une exception, donc l'élément n'existe pas

    def _isNeighbor(self, x:int, y:int) ->bool :
        if self._isExist(x, y) and self.gameboard[x][y] == 1 :
            return True
        else :
            return False


    def iterate(self) :
        self._iteration += 1
        for x in range(self._size) :
            for y in range(self._size) :
                neighbors = 0
                if self._isNeighbor(x-1, y-1) : neighbors += 1
                if self._isNeighbor(x, y-1) : neighbors += 1
                if self._isNeighbor(x+1, y-1) : neighbors += 1

                if self._isNeighbor(x+1, y) : neighbors += 1
                if self._isNeighbor(x-1, y) : neighbors += 1

                if self._isNeighbor(x-1, y+1) : neighbors += 1
                if self._isNeighbor(x, y+1) : neighbors += 1
                if self._isNeighbor(x+1, y+1) : neighbors += 1

                if neighbors < 2 :
                    # DIE : UNDER POPULATION
                    self.gameboard[x][y] = 0
                elif neighbors == 3 :
                    # BORN
                    self.gameboard[x][y] = 1
                elif neighbors > 3 :
                    # DIE : OVER POPULATION
                    self.gameboard[x][y] = 0

    def save_file(self) :
        file = "./saves/file.txt"
    def load_file(self) :
        pass
            


    def generateShuffleGameboard(self, margin: int = 4):
        # Créer une matrice remplie de 0
        self.gameboard = [[0 for _ in range(self._size)] for _ in range(self._size)]

        # Définir les limites du centre (par exemple, le quart central de la matrice)
        margin = self._size // margin  # Vous pouvez ajuster la taille du centre ici
        start = margin
        end = self._size - margin

        # Remplir le centre avec des valeurs aléatoires
        for i in range(start, end):
            for j in range(start, end):
                self.gameboard[i][j] = random.randint(0, 1)


    def printGameBoard(self) :
        for i in range(self._size) :
            string = ""
            for j in range(self._size) :
                if self.gameboard[i][j] == 0 :
                    string += "🔲"
                elif self.gameboard[i][j] == 1 :
                    string += "⬛"
            print(string)
    
    def get_iteration(self) -> int : return self._iteration

args = getargs()
SIZE = args.size
ITERATIONS = args.iterations
SEED = args.seed
if SEED == None :
    SEED = random.seed()
else :
    random.seed(SEED)

print()
gameboard = GameBoard(SIZE)
gameboard.generateShuffleGameboard(margin=3)

historic = []
for i in range(ITERATIONS+1) :
    historic.append(gameboard.gameboard)
    gameboard.printGameBoard()
    print(f"Iteration n°{gameboard.get_iteration()}/{ITERATIONS}")
    print(f"Seed : {SEED}")
    sleep(0.1)
    gameboard.iterate()

    #if i > 3 :
    #    if historic[i-2] == historic[i] :
    #        print("The simulation is on boucle")
    #        break