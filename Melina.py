i

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
            
            if isinstance(animal, Sheep):
                animal.age += 1
                
                # Regarde si on est sur de l'herbe
                if dico[key][0].existence == 1:
                   animal.energy += 15
                   
                # Regarde les voisins pour voir s'il y a de l'herbe"""
                l_grass = []
                if (x+1,y) in dico and dico[(x+1,y)][0].existence == 1:
                   l_grass.append((x+1,y))
                elif (x-1,y) in dico and dico[(x-1,y)][0].existence == 1:
                   l_grass.append((x-1,y))
                elif (x,y+1) in dico and dico[(x,y+1)][0].existence == 1:
                   l_grass.append((x,y+1))
                elif (x,y-1) in dico and dico[(x,y-1)][0].existence == 1:
                   l_grass.append((x,y-1))
                
                if len(l_grass) > 0:
                    new_pos = random.choice(l_grass)
                elif len(l_grass) == 0:
                    # Déplace le mouton
                    l_move = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
                    
    
                dic_new[new_pos] = (dico[new_pos][0], animal)
                dic_new[key] = (dico[key][0], None)
                                  
        dico[key] = dic_new[key]
               
class Wolf():
    def __init__(self, age, energy):
        self.age = age
        self.energy = energy
 
 
