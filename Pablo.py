import pyxel 
import random
#from Nathan import Grass
#from Melina import Sheep
#from Melina import Wolf


class Grass:
    def __init__(self,existence,regeneration):
        self.existence=existence
        self.regeneration=regeneration
    
    def update(self):
        if self.existence==0 and self.regeneration!=-1: 
            self.regeneration+=1
        if self.regeneration==7:
            self.existence=1
        if self.existence==0 and self.regeneration==-1: #fais spawn de l'herbe aléatoirement
            if random.random() <=0.05 : 
                self.existence=1
                self.regeneration=0

class Sheep:
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy

class Wolf:
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy

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
        self.update_grass()
        
    def update_grass(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                Grass.update(self.grille[(x,y)][0])
    
    def draw(self):
        pyxel.cls(0)
        self.draw_grille()
        self.draw_animal()
        

    def grid_initiale(self):
        grille = {(x,y):[Grass(0,-1),None] for x in range(GRID_SIZE) for y in range(GRID_SIZE)} 
        n = 0
        m = 0
        l = 0
        surface = (GRID_SIZE**2)*INITIAL_GLASS_COVERAGE
        while n <= surface:
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][0].existence == 0 :
                grille[(i,j)][0].existence = 1
                n+=1
        while m <= INITIAL_SHEEP :
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][1] == None:
                grille[(i,j)][1] = Sheep("mouton",0,20)
                m+=1
        while l <= INITIAL_WOLVES : 
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][1] == None:
                grille[(i,j)][1] = Wolf("loup",0,40)
                l+=1
        print(grille)
        return grille
        
    

    
    def draw_grille(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grille[(x,y)][0].existence == 1 :
                    color = 11
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
                else :
                    color = 4
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
            
    def draw_animal(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grille[(x,y)][1] != None : 
                    if self.grille[(x,y)][1].type =="mouton":
                        pyxel.blt(x*SIDE,y*SIDE,0,0,0,SIDE,SIDE, colkey=0)
                    elif self.grille[(x,y)][1].type =="loup":
                        pyxel.blt(x*SIDE,y*SIDE,0,0,SIDE,SIDE,SIDE, colkey=7)


if __name__ == "__main__":
    Grid()
