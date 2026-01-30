Pour le choix de la structure : 
on utilise le dictionnaire : grille
dont les clés sont les coordonnées (x,y)
les valeurs sont une liste : [herbe, animal]
herbe est un élément de la classe Grass
animal est un élément de la classe Wolf ou Sheep OU animal = None s'il n'y a pas d'animal sur cette case

Class Grid : 
- Méthodes : grid_initiale (initialise la grille), update (update_sheep, update_wolf, update_grass) (mise à jour de la grille), draw (draw_grille) (affichage de la grille)

Classe Grass :
- existence : booléen : 0 si pas d'herbe, 1 si de l'herbe
- regeneration : int : -1 si jamais eu d'herbe, 0 si herbe mais non mangée, 1 à 7 si l'herbe vient d'être mangée, et on incrémente à chaque tour de 1, à 7 l'herbe a repoussé. 
- méthode update pour mettre à jour à chaque instant l'état de l'herbe

Classe Sheep :
- type : pour faciliter les tests lors des mises à jour (en réalisant "if animal.type == 'mouton'")
- age
- energie
- Méthodes : update (idée : parcourt le dictionnaire grille [en utilisant un dictionnaire intermédiaire] et lorsqu'on tombe sur un mouton en (x,y), on met à jour l'état du mouton), Mort, Reproduction, OnGrass (vérifier si le mouton est sur de l'herbe et, si oui, la manger), Move (déplacer le mouton)

Classe Wolf :
- type : pour faciliter les tests lors des mises à jour (en réalisant "if animal.type == 'loup'")
- age
- energie
- Méthodes : update, Mort, Reproduction, MangeAdjSheep (teste si le loup est proche à distance 1 d'un mouton et, si oui, le mange), Move (déplacer le loup)

TRAVAIL EFFECTUE : 
Pablo : positionnement initial des animaux, graphisme des animaux, classe Wolf
Pauline : affichage (classe Grid), lien entre classes et modifications, classe Wolf
Melina : classe Sheep, Début classe Wolf, gestion des problèmes liés aux dictionnaires intermédiaires
Nathan : structure des données, classe herbe, gestion des problèmes liés aux dictionnaires intermédiaires, tracés des données
Tous : Réflexion sur la structure globale du projet, amélioration des classes, fonctions, méthodes
