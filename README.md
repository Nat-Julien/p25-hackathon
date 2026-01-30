Pour le choix de la structure : 
on utilise le dictionnaire : grille
dont les clés sont les coordonnées (x,y)
les valeurs sont une liste : [presence_herbe,age_herbe,(animal,age_animal,energie_animal)]

- presence_herbe : booléen : 0 si pas d'herbe, 1 si de l'herbe
- age_herbe : int : -1 si jamais eu d'herbe, 0 si herbe mais non mangée, 1 à 7 si l'herbe vient d'être mangée, et on incrémente à chaque tour de 1, à 7 l'herbe a repoussé. 
- animal : "loup", "mouton" ou None
- age_animal : int age de l'animal, et si pas d'animal sur la case : None
- energie_animal : int ernergie de l'animal, et si pas d'animal sur la case : None
