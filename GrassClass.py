import random

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