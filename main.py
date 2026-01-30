#Importation des bibliothèques. Utilisation de Pyxel pour l'interface
import pyxel 
import random
from copy import deepcopy

class Grass:
    def __init__(self,existence,regeneration): #Classe Herbe avec Existence
        self.existence=existence #Présence sur une case (booléen : 0 si absent, 1 si herbe à manger)
        self.regeneration=regeneration # -1 si toujours pas mangé, Chiffre de 1 à 7 si mangé au moment 0 (7 tours avant regénération)
    
    def update(self):
        if self.existence==0 and self.regeneration!=-1: #L'herbe a été mangée précedemment, donc on incrémente vers la génération
            self.regeneration+=1
        if self.regeneration==7: #Les 7 tours sont passés d'où l'herbe repousse
            self.existence=1
        if self.existence==0 and self.regeneration==-1: #Fait apparaître de l'herbe aléatoirement parmi les endroits où il n'y a jamais eu d'herbe
            if random.random() <=0.05 : 
                self.existence=1
                self.regeneration=0

class Sheep:
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy
    
    def update(self, dico):
        dic_new = deepcopy(dico)
        
        for key in dico:
            x, y = key
            l_free=[]
            animal = dico[key][1]
            herbe = dico[key][0]
            if (x+1,y) in dico and dic_new[(x+1,y)][1] is None:
                l_free.append((x+1,y))
            if (x-1,y) in dico and dic_new[(x-1,y)][1] is None :
                l_free.append((x-1,y))
            if (x,y+1) in dico and dic_new[(x,y+1)][1] is None:
                l_free.append((x,y+1))
            if (x,y-1) in dico and dic_new[(x,y-1)][1] is None:
                l_free.append((x,y-1)) # Mouvements possibles
            
            if dico[key][1]!= None and animal.type == "mouton":
                animal.OnGrass(dico,key)
                animal.age += 1
                animal.Mort(dico,key,dic_new)
                if animal.energy > 50:
                    animal.Reproduction(dico,key,l_free,dic_new)

                animal.Move(dico,dic_new,key, l_free)
        return (deepcopy(dic_new))
               
               
    def Mort(self,dico,key,dic_new):
        animal = dico[key][1]
        if animal.age > 50 or animal.energy <= 0:
            dic_new[key] = (dico[key][0], None)
                    
    
    def OnGrass(self,dico,key):
        if dico[key][0].existence == 1:
                self.energy += 15
                dico[key][0].existence = 0
                dico[key][0].regeneration = 0
                
    def Reproduction(self,dico,key,l_free,dic_new):
        new_sheep = Sheep('mouton', 0, 20)

        if len(l_free)>0 :
            pos_baby = random.choice(l_free)
            dic_new[pos_baby] = (dico[pos_baby][0], new_sheep)
            
    def Move(self,dico,dic_new,key,l_free):
        animal = dico[key][1]
        # Regarde les voisins pour voir s'il y a de l'herbe"""
        l_grass = []
        x, y = key
        if (x+1,y) in dico and dico[(x+1,y)][0].existence == 1:
            l_grass.append((x+1,y))
        if (x-1,y) in dico and dico[(x-1,y)][0].existence == 1:
            l_grass.append((x-1,y))
        if (x,y+1) in dico and dico[(x,y+1)][0].existence == 1:
            l_grass.append((x,y+1))
        if (x,y-1) in dico and dico[(x,y-1)][0].existence == 1:
            l_grass.append((x,y-1))
                
        if len(l_grass) > 0:
            new_pos = random.choice(l_grass)
            dic_new[new_pos] = (dico[new_pos][0], animal)
            dic_new[key] = (dico[key][0], None)
        elif len(l_grass) == 0 and len(l_free) > 0:
            # Déplace le mouton
            new_pos = random.choice(l_free)  
            dic_new[new_pos] = (dico[new_pos][0], animal)
            dic_new[key] = (dico[key][0], None)
        

class Wolf:
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy
    
    def update(self, dico):
        dic_new = dico.copy()
        for key in dico:
            x, y = key
            l_free=[]
            animal = dico[key][1]
            herbe = dico[key][0]
            if (x+1,y) in dico and dic_new[(x+1,y)][1] is None:
                l_free.append((x+1,y))
            if (x-1,y) in dico and dic_new[(x-1,y)][1] is None:
                l_free.append((x-1,y))
            if (x,y+1) in dico and dic_new[(x,y+1)][1] is None:
                l_free.append((x,y+1))
            if (x,y-1) in dico and dic_new[(x,y-1)][1] is None:
                l_free.append((x,y-1)) # Mouvements possibles
            
            if dico[key][1]!= None and animal.type == "loup":
                
                animal.age += 1
                animal.energy -=1
                
                animal.Mort(dico,key,dic_new)
                animal.MangeAdjSheep(dico,key)
            
                if animal.energy > 80:
                    animal.Reproduction(dico,key,l_free)
            
                animal.Move(dico,key, l_free)
        dico = deepcopy(dic_new)                  
        
        return dico
    def Mort(self,dico,key,dic_new):
        animal = dico[key][1]
        if animal.age > 50 or animal.energy <= 0:
            dic_new[key] = (dico[key][0], None)
    def MangeAdjSheep(self,dico,key):
        l_adj=[]
        x,y=key
        Ate_sheep=False
        key_ate_sheep=None
        for d in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if d in dico and dico[d][1]!= None and dico[d][1].type=="mouton":
                    l_adj.append(d)
        if l_adj!=[]:
            key_ate_sheep=random.choice(l_adj)
            Ate_sheep=True
            self.energy += 30
            dico[key_ate_sheep] = (dico[key][0],None)
        return (Ate_sheep,key_ate_sheep)
                
    def Reproduction(self,dico,key,l_free):
        if self.energy > 80 and l_free != []:
            self.energy -=20
            new_wolf = Wolf('loup', 0, 40)
            pos_baby = random.choice(l_free)
            dico[pos_baby] = (dico[pos_baby][0], new_wolf)
        
            
    def Move(self,dico,key, l_free):
        Ate_sheep, key_ate_sheep = self.MangeAdjSheep(dico,key)
        animal = dico[key][1]
        new_pos=key
        if Ate_sheep :
            new_pos = key_ate_sheep
        elif len(l_free)>0 : 
            new_pos = random.choice(l_free)
        if new_pos != key : 
            dico[new_pos] = (dico[new_pos][0], animal)
            dico[key] = (dico[key][0], None)

#configuration initiale
GRID_SIZE = 20
SIDE = 16
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GLASS_COVERAGE  = 0.3 #30% de la surface est couverte par de l'herbe 

class Grid : 
    #INITIALISATION
    def __init__(self):
        pyxel.init(GRID_SIZE*SIDE,GRID_SIZE*SIDE,fps = 10, title = "Ecosystème")
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