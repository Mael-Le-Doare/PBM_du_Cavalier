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
    # boucles du graphe
    boucle : int =0

    def __init__(self, n : str, sA : list) :
        # on assigne le nom et les sommet adjacents passés en parametre
        self.nom = n
        self.sommetAdjacents=sA

        # pour chacun des sommets rencontontrés on incrémente le degré du sommet
        self.initDegre()
    
    def __str__(self):
        # affichage de notre objet sommet
        return f"{self.nom}"
    
    
    def afficherAdjacents(self):
        chaineSortie : str = f"Sommets adjacents de {self.nom} ="
        # affichage des sommets adjacents
        for sommet in self.sommetAdjacents.items():
            chaineSortie+=f" | sommet : {sommet[0]} poids : {(sommet[1])}"
        print(chaineSortie+" |")
    
    def retourneDegre(self)->int:
        #renvoie la valeur (entier) du degre de notre sommet
        return self.degre
    
    def retourneBoucle(self)->int:
        return self.boucle
    
    def initAdjacents(self, dico : dict):
        # methode pour actualiser le dictionnaire des sommets adjacents
        self.sommetAdjacents.update(dico)
        self.initDegre()
    
    def initDegre(self)->int:
        #initianalise les degre du sommet
        for sommets in self.sommetAdjacents:
            self.degre +=1
            #si l'on rencontre une boucle le degré de notre sommet est incrémenté de 2
            if sommets.nom==self.nom:
                self.degre +=1
                #on incremente egalement le nombre de boucle de notre sommet
                self.boucle +=1
    
    def estIsole(self)->bool:
        return self.sommetAdjacents=={}


