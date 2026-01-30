class Sheep():
    def __init__(self, age, energy):
        self.age = age
        self.energy = energy
    
    """ UPDATE PAS FINI
    def update(self, dico):
        dic_new = dico.copy()
        for key in dico:
            
            x, y = key
            animal = dic_new[key][2]
            
            if animal[0] == 'Sheep':
                self.age += 1
                dic_new[key][3] = self.age
                dico[key] = dic_new[key]
               
                # Regarde si on est sur de l'herbe
                if dico[key][0] == 1:
                   self.energy += 15
                   dico[key][4] = self.energy
                   
               # Regarde les voisins pour voir s'il y a de l'herbe"""
               
class Wolf():
    def __init__(self, age, energy):
        self.age = age
        self.energy = energy
               
               