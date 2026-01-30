import random
from copy import deepcopy

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
                animal.energy -= 2
                
                animal.Mort(dico,key,dic_new)
                animal.MangeAdjSheep(dico,key)
            
                if animal.energy > 80:
                    animal.Reproduction(dico,key,l_free)
            
                animal.Move(dico,key, l_free)
        dico = deepcopy(dic_new)                  
        
        return dico
    def Mort(self,dico,key,dic_new):
        animal = dico[key][1]
        if animal.age > 40 or animal.energy <= 0:
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