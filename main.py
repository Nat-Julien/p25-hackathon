#Importation des bibliothèques. Utilisation de Pyxel pour l'interface
import pyxel 
import random
from GrassClass import Grass
from SheepClass import Sheep
from WolfClass import Wolf

#configuration initiale
GRID_SIZE = 50
SIDE = 16
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GLASS_COVERAGE  = 0.3 #30% de la surface est couverte par de l'herbe 

class Grid : 
    #INITIALISATION
    def __init__(self):
        pyxel.init(GRID_SIZE*SIDE,GRID_SIZE*SIDE, title = "Ecosystème")
        pyxel.load("Dessins.pyxres") #Dessin des loups et moutons
        self.grille = self.grid_initiale() #Initialisation de la grille par la fonction ci-dessous
        pyxel.run(self.update,self.draw)
    
    #Initialisation de la grille = dico avec CLES=Position (x,y) des cases ; Valeurs [Herbe, Animal]
    def grid_initiale(self):
        grille = {(x,y):[Grass(0,-1),None] for x in range(GRID_SIZE) for y in range(GRID_SIZE)} 
        n = 0
        m = 0
        l = 0
        surface = (GRID_SIZE**2)*INITIAL_GLASS_COVERAGE #On veut 30% de la surface initiale couverte d'herbe
        while n <= surface: 
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][0].existence == 0 :
                grille[(i,j)][0].existence = 1
                n+=1
        while m <= INITIAL_SHEEP : #Placement de mouton aléatoire
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][1] == None:
                grille[(i,j)][1] = Sheep("mouton",0,20)
                m+=1
        while l <= INITIAL_WOLVES : #Placement de loup aléatoire
            i,j = random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)
            if grille[(i,j)][1] == None:
                grille[(i,j)][1] = Wolf("loup",0,40)
                l+=1
        return grille

    #ACTUALISATION
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q): #pour quitter le jeu (la croix fonctionne aussi)
            pyxel.quit()
        self.draw() #Fonction dessin
        self.update_grass()  #Actualisation de l'herbe
        self.update_sheep()
        self.update_wolf()
        
    def update_grass(self): 
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                Grass.update(self.grille[(x,y)][0])
    
    def update_sheep(self):
        self.grille=Sheep.update(self,self.grille)

    def update_wolf(self):
        Wolf.update(self,self.grille)



    #DESSIN
    #Fonction dessin
    def draw(self):
        pyxel.cls(0)
        self.draw_grille() #Dessin de grille (à tout instant t) Cases + Herbe + Animaux 
    
    #Dessiner la grille avec l'herbe + Animaux
    def draw_grille(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grille[(x,y)][0].existence == 1 :
                    color = 11
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
                else :
                    color = 4
                    pyxel.rect(x*SIDE, y*SIDE, SIDE, SIDE, color)
                if self.grille[(x,y)][1] != None : 
                    if self.grille[(x,y)][1].type =="mouton":
                        pyxel.blt(x*SIDE,y*SIDE,0,0,0,SIDE,SIDE, colkey=0) #Dessin depuis le fichier dessin
                    elif self.grille[(x,y)][1].type =="loup":
                        pyxel.blt(x*SIDE,y*SIDE,0,0,SIDE,SIDE,SIDE, colkey=7) #Idem


if __name__ == "__main__":
    Grid()