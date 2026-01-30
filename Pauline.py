import pyxel 

#configuration initiale
GRID_SIZE = 20
CASES = 16
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GLASS_COVERAGE  = 0.3 #30% de la surface est couverte par de l'herbe 

class Grid : 

    def __init__(self):
        pyxel.init(GRID_SIZE*CASES,GRID_SIZE*CASES,title = "Ecosystème")
        pyxel.run(self.update,self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): #pour quitter le jeu (la croix fonctionne aussi)
            pyxel.quit()
        self.draw()
    
    def draw(self):
        pyxel.cls(0)
    
    def grid_initiale(self):
        cases = {(x,y):[0,-1,None,None,None] for x in range(GRID_SIZE) for y in range(GRID_SIZE)} 
        #(position):[0 si rien, 1 si herbe; age herbe (-1 si jamais eu herbe);"mouton ou loup" ou None;age mouton/age loup (ou None); energy]
        n = 0
        surface = GRID_SIZE*INITIAL_GLASS_COVERAGE
        while n < surface:

if __name__ == "__main__":
    Grid()
