import sommet
import constantes
import entities

class Graphe: 

    def __init__(self, ordre : int):
        #creation de tout les sommets et initianalisation de l'ordre du graphe
        self.ordre=0
        self.sommets=[]
        self.initGraph(ordre)

    
    def initGraph(self, ordre : int):
        #methode qui remplie la liste des sommets celon la convention classique du nommage des cases d'un plateau d'echec
        ligne : list = []
        for lettre in range(1,ordre+1):
            for i in range(1,ordre+1):
                #les sommet auront un nom du type : E4, A2, F7...
                #on n'initianalise pas encore leur sommets adjacents
                ligne.append(sommet.Sommet(chr(lettre+64)+str(i),[]))
                #actualise egalement l'ordre du graphe
                self.ordre+=1
            #on ajoute notre ligne
            self.sommets.append(ligne)
            #on vide notre liste
            ligne=[]
        self.initSommetsAdjecents()

    def afficheSommets(self):
        #affichage de tout les sommets du graphes
        for i in self.sommets:
            for j in i:
                print(j)
    
    def estValide(self, x : int, y : int)->bool:
        #renvoie si la case de coordones (x,y) a ete visite (true si non visitee; false sinon)
        return not(self.sommets[x][y].estVisite)

    
    def initSommetsAdjecents(self):
        #fonction qui pour chaque sommet du graphe, renseigne ses sommets adjacents
        #creation de notre piece cavalier
        piece= entities.Piece(0,0, constantes.knight)
        #creation de notre plateau
        pl=entities.Plateau(len(self.sommets),len(self.sommets),piece)
        for y in range(len(self.sommets)):
            for x in range(len(self.sommets)):
                pl.piece.position.x = x
                pl.piece.position.y = y
                #on creer une liste contenant tout les deplacements possibles de notre cavalier
                liste=pl.bouger()
                for i in liste:
                    #on renseigne au sommet de coordonnes(x,y) dans notre liste de sommet les sommets adjacents correspondant aux deplacement
                    self.sommets[x][y].initAdjacents(i.getMat(self.sommets))
    
    def existe(self, nomSommet : str) -> tuple:
        #retourne les coordonnes d'une case dans la matrice self.listeSommets
        #l'abscisse correspond au code ASCII de la case -65 (car ici on est en majuscule)
        x = ord(nomSommet[0])-ord(chr(65)) 
        #l'ordonee correspond au chiffre de la case -1 (car le premier indice est 0) 
        y = int(nomSommet[1:])-1        
    
        #on verifie que les coordonnes appartiennent bien au graphe
        if 0 <= x < len(self.sommets) and 0 <= y < len(self.sommets):
            return (x, y)
    
        return (None, None)
    

    def DFS(self, nomSommet : str, listeSortie : list) -> bool:
        #La fonction qui nous permet de resoudre le probleme du cavalier avec un parcours en profondeur et la methode Warnsdorff
        #ici on ne cherche pas à réaliser un cycle
        #on recupere les coordonees du sommet grace à son nom passé en parametre
        cooSommetActuel : tuple = self.existe(nomSommet)

        #si le sommet n'est pas dans le graphe alors on arrete le parcours
        if cooSommetActuel == (None, None):
            return False

        #grace aux coordonees recuperees, on obtient notre sommet courant
        sommetActuel : sommet = self.sommets[cooSommetActuel[0]][cooSommetActuel[1]]

        #notre condition d'arret : on arrete les appelles recursif quand on a trouver un chemin hamiltonien 
        if len(listeSortie) == self.ordre:
            return True
        # on creer une liste conteant tout les sommets/cases ajacents à notre sommet courant
        voisins : list = sommetActuel.sommetAdjacents[:]
        # on applique la methode de tri de Warnsdorff ce qui optimise grandement notre parcours
        #on tri les voisins suivant leur nombre de voisins pour choisir la case qui possède le moins de coups suivants  (gain de temps énorme)
        voisins.sort(key=lambda v: sum(
        1 for sommets in v.sommetAdjacents
        if not self.sommets[self.existe(sommets.nom)[0]][self.existe(sommets.nom)[1]].estVisite))
        
        #maintenant notre liste triee, on parcours les voisins
        for voisin in voisins:
            #on recupère leur coordonees dans notre matrice
            cooVoisins = self.existe(voisin.nom)
        
            #si ils ne sont pas déjà visitées, on les ajoutes a notre liste et on les met comme visite
            if not self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite:
                listeSortie.append(voisin.nom)
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = True

                #appel récursif
                if self.DFS(voisin.nom, listeSortie):
                    return True

                #si l'appel recursif ne renvoie pas true, alors le chemin est mauvais 
                #alors on retire ce sommet de notre liste
                listeSortie.pop()
                #on le remet comme non visite
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = False
    
        return False
    
    def DFSCycle(self, nomSommet : str, nomDepart : str, listeSortie : list) -> bool:
        #La fonction qui nous permet de resoudre le probleme du cavalier avec un parcours en profondeur et la methode Warnsdorff
        #ici on ne cherche à réaliser un cycle
        #on recupere les coordonees du sommet grace à son nom passé en parametre
        cooSommetActuel : tuple = self.existe(nomSommet)

        #si le sommet n'est pas dans le graphe alors on arrete le parcours
        if cooSommetActuel == (None, None):
            return False

        #grace aux coordonees recuperees, on obtient notre sommet courant
        sommetActuel : sommet = self.sommets[cooSommetActuel[0]][cooSommetActuel[1]]

        #notre condition d'arret : on arrete les appelles recursif quand on a trouver un chemin hamiltonien qui revient au point de depart
        if len(listeSortie) == self.ordre:
            cooDepart = self.existe(nomDepart)
            sommetDepart = self.sommets[cooDepart[0]][cooDepart[1]]
            if sommetDepart in sommetActuel.sommetAdjacents:
                return True
            else:
             return False
        # on creer une liste conteant tout les sommets/cases ajacents à notre sommet courant
        voisins : list = sommetActuel.sommetAdjacents[:]
        # on applique la methode de tri de Warnsdorff ce qui optimise grandement notre parcours
        #on tri les voisins suivant leur nombre de voisins pour choisir la case qui possède le moins de coups suivants  (gain de temps énorme)
        voisins.sort(key=lambda v: sum(
        1 for sommets in v.sommetAdjacents
        if not self.sommets[self.existe(sommets.nom)[0]][self.existe(sommets.nom)[1]].estVisite))
        
        #maintenant notre liste triee, on parcours les voisins
        for voisin in voisins:
            #on recupère leur coordonees dans notre matrice
            cooVoisins = self.existe(voisin.nom)
        
            #si ils ne sont pas déjà visitées, on les ajoutes a notre liste et on les met comme visite
            if not self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite:
                listeSortie.append(voisin.nom)
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = True

                #appel récursif
                if self.DFSCycle(voisin.nom,nomDepart, listeSortie):
                    return True

                #si l'appel recursif ne renvoie pas true, alors le chemin est mauvais 
                #alors on retire ce sommet de notre liste
                listeSortie.pop()
                #on le remet comme non visite
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = False
    
        return False


    def convertionDFS(self, liste : list)->list:
        #cette methode renvoie la liste de parcours sous forme de coordonnes pour gerer notre affichage
        listeSortie: list = []
        for i in liste:
            #par exemple la case "A1" sera convertie en (0,0) avec notre methode self.existe()
            listeSortie.append(self.existe(i))
        return listeSortie





