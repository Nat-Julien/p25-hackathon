import random
class Grass :
    def __init__(self,existence,regeneration):
        self.existence=existence
        self.regeneration=regeneration

    def update(self):
        if self.existence==0 and self.regeneration!=-1: 
            self.regeneration+=1
        if self.regeneration==7:
            self.existence=1
        if self.existence==0 and self.regeneration==-1: #fais spawn de l'herbe aléatoirement
            if random()<=0.05 : 
                self.existence=1 and self.regeneration=0
    def est_mange(self):
        self.existence==0
        self.regeneration==0
