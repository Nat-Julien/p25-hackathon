
import pyxel 
import random


#COULEURS
BLACK=0
WHITE=7
#configuration initiale
GRID_SIZE = 20
SIDE = 16
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GLASS_COVERAGE  = 0.3 #30% de la surface est couverte par de l'herbe 

class Grid : 
    def __init__(self):
        pyxel.init(GRID_SIZE*SIDE,GRID_SIZE*SIDE,title = "Ecosystème")
        pyxel.load("Dessins.pyxres")
        self.grille = self.grid_initiale()
        pyxel.run(self.update,self.draw)
        
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): #pour quitter le jeu (la croix fonctionne aussi)
            pyxel.quit()
        self.draw()
    
    def draw(self):
        pyxel.cls(0)
        self.draw_grille()


    
    def grid_initiale(self):
        grille = {(x,y):[0,-1,'',None,None] for x in range(GRID_SIZE) for y in range(GRID_SIZE)} 
        #(position):[0 si rien, 1 si herbe; age herbe (-1 si jamais eu herbe);("mouton ou loup" ou None;age mouton/age loup (ou None); energy)]
        n = 0
        m = 0
        l = 0
        surface = (GRID_SIZE**2)*INITIAL_GLASS_COVERAGE
        while n < surface:
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][0] == 0 :
                grille[(i,j)][0] = 1
                n+=1
        while m < INITIAL_SHEEP :
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][2]=='':
                grille[(i,j)][2] = "mouton"
                m+=1
        while l < INITIAL_WOLVES : 
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][2]=='':
                grille[(i,j)][2] = "loup"
                l+=1
        print(grille)
        return grille
    
    def draw_grille(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grille[(x,y)][0] == 1 :
                    color = 11
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
                elif self.grille[(x,y)][0]==0: 
                    color = 4
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
                if self.grille[(x,y)][2]=="mouton":
                    pyxel.blt(x*SIDE,y*SIDE,0,0,0,SIDE,SIDE, colkey=BLACK)
                elif self.grille[(x,y)][2]=="loup":
                    pyxel.blt(x*SIDE,y*SIDE,0,0,SIDE,SIDE,SIDE, colkey=WHITE)
        pyxel.blt(0,0,0,0,0,SIDE,SIDE,colkey=BLACK)
                

if __name__ == "__main__":
    Grid()