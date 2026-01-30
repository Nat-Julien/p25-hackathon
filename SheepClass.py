import random
from copy import deepcopy

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