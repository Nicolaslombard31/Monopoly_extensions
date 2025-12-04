from typing import List

class Quartier:
    def __init__(self, couleur, prix_maison):
        self.couleur = couleur
        self.prix_maison = prix_maison
        self.proprietes = List['Propriete'] = []
    
    def posserderQuartier(self, j: 'Joueur'):
        nb_propriete = len(self.proprietes)
        nb_propriete_j = 0
        for propiete in j.propietes:
                if isinstance(propiete, j.proprietes) and propiete.couleur == self.couleur:
                    nb_propriete_j += 1
        
        return nb_propriete_j == nb_propriete