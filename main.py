# On définit une classe sommet
class Sommet:
    # nom du sommet
    nom : str = ""
    # dictionnaire des sommet adjacents (la clef etant le sommet et la valeur designe le poids de l'arrette)
    sommetAdjacents : dict = {}
    # le sommet a t'il ete visite ?
    estVisite : bool = False
    # degré du graph
    degre : int = 0

    def __init__(self, n : str, sA : list) :
        # on assigne le nom et les sommet adjacents passés en parametre
        self.nom = n
        self.sommetAdjacents=sA

        # pour chacun des sommets rencontontrés on incrémente le degré du sommet
        for sommets in self.sommetAdjacents:
            self.degre +=1

    
    def __str__(self):
        # affichage de notre objet sommet
        return f"{self.nom}"
    
    
    def afficherAdjacents(self):
        # affichage des sommets adjacents avec
        for sommet in self.sommetAdjacents.items():
            print((sommet)[0],sommet[1])
    
    def initAdjacents(self, dico : dict):
        # methode pour actualiser le dictionnaire des sommets adjacents
        self.sommetAdjacents.update(dico)


A=Sommet("A",{})
B=Sommet("B",{})
C=Sommet("C",{})
A.initAdjacents({B:3,C:8})
B.initAdjacents({A:3,C:5})
C.initAdjacents({A:8,B:5})
A.afficherAdjacents()
B.afficherAdjacents()
C.afficherAdjacents()