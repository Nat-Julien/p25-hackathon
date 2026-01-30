import random as rd

class Sheep():
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy
    
    def update(self, dico):
        dic_new = dico.copy()
        
        for key in dico:
            x, y = key
            animal = dico[key][1]
            herbe = dico[key][0]
            l_move = [(x+1,y) if (x+1,y) in dico, (x-1,y) if (x-1,y) in dico, (x,y+1)if (x,y+1) in dico, (x,y-1)if (x,y-1) in dico] # Mouvements possibles
            
            if animal.type == 'mouton':
                animal.age += 1
                
            animal.Mort(dico,key)
            animal.OnGrass(dico,key)
                
            # Cherche les cases libres autour 
            l_free = [] 
            for elem in l_move:
                if dico[elem][1] is None:
                    l_free.append(elem)
            
            if animal.energy > 50:
                animal.Reproduction(dico,key)
            
            animal.Move(dico,dic_new,key, l_free)
                                  
        dico[key] = dic_new[key]
               
               
    def Mort(self,dico,key):
        animal = dico[key][1]
        if animal.age > 50 or animal.energy <= 0:
                    dic_new[key] = (dico[key][0], None)
                    
    
    def OnGrass(self,dico,key):
        if dico[key][0].existence == 1:
                self.energy += 15
                dico[key][0].existence = 0
                
    def Reproduction(self,dico,key):
        x, y = key
        l_reprod = []
        if (x+1,y) in dico and dico[(x+1,y)][1] and dico[(x+1,y)][1].type == 'mouton':
            l_reprod.append((x+1,y))
        elif (x-1,y) in dico and dico[(x-1,y)][1] and dico[(x-1,y)][1].type == 'mouton':
            l_reprod.append((x-1,y))
        elif (x,y+1) in dico and dico[(x,y+1)][1] and dico[(x,y+1)][1].type == 'mouton':
            l_reprod.append((x,y+1))
        elif (x,y-1) in dico and dico[(x,y-1)][1] and dico[(x,y-1)][1].type == 'mouton':
            l_reprod.append((x,y-1))
                    
        if len(l_reprod) > 0:
            self.energy -= 20
            new_pos = rd.choice(l_reprod)
            new_sheep = Sheep('mouton', 0, 20)
            
    def Move(self,dico,dic_new,key, l_free):
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
            new_pos = rd.choice(l_grass)
        if len(l_grass) == 0:
            # Déplace le mouton
            new_pos = rd.choice(l_free) # VÉRIFIER QUEE LA CASE EST LIBRE ET DANS LE CADRE!!!!!!!!!!!!!!!!!!!!
            
        dic_new[new_pos] = (dico[new_pos][0], self) # RETIRER L'ANIMAL DE SA CASE ACTUELLE !!!!!!!!!!!!!!!!!!!
        dic_new[key] = (dico[key][0], None)
        
    
    
        
    
class Wolf():
    def __init__(self, type, age, energy):
        self.type = type
        self.age = age
        self.energy = energy
 
 
