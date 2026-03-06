import sommet
import constantes
import entities

class Graphe: 
    #la matrice a deux dimensions de tout les sommet
    sommets : list = []
    #nombre de Sommet:
    ordre : int = 0

    def __init__(self, ordre : int):
        #creation de tout les sommets et initianalisation de l'ordre du graphe
        self.initGraph(ordre)

    
    def initGraph(self, ordre : int):
        #methode qui remplie la liste des sommets celon la convention classique du nommage des cases d'un plateau d'echec
        ligne : list = []
        for lettre in range(1,ordre+1):
            for i in range(1,ordre+1):
                #les sommet auront un nom du type : E4, A2, F7...
                #on n'initianalise pas encore leur sommets adjacents
                ligne.append(sommet.Sommet(chr(lettre+64)+str(i),{}))
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
                    self.sommets[x][y].initAdjacents({i.getMat(self.sommets):0})
    
    
    def DFS(self, nomSommet : str, listeSortie : list)->list:
        #renvoie une liste resultant du parcours en largeur du graphe
        #on traite le sommet actuel
        sommetActuel : sommet = self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]]
        #si il n'est pas dans notre liste de parcours et qu'il n'est pas visité alors :
        if sommetActuel.nom not in listeSortie and not sommetActuel.estVisite:
            #on l'ajoute à notre liste
            listeSortie.append(sommetActuel.nom)
            #on le marque comme visité
            self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]].estVisite=True
        else:
            #sinon on ne l'ajoute pas (on ne fait rien)
            return
        for voisins in sommetActuel.sommetAdjacents.keys():
            #tant que notre sommet a des voisins adjacents
            #on traite ce sommet en passant notre liste actualisée en paramètre
            self.DFS(voisins.nom,listeSortie)

    def existe(self, nomSommet : str)->tuple:
        #methode qui verifie que le sommet est bien present dans le graphe et renvoie ses coordonees
        #on parcours les colonnes
        for i in range(len(self.sommets)):
            #on parcours les lignes
            for j in range(len(self.sommets)):
                #si on le trouve on renvoie un tuple contenant sa position (x,y)
                if self.sommets[i][j].nom == nomSommet:
                    return (i,j)
        #sinon on renvoie un tuple "nul"
        return (None,None)




monGraphe = Graphe(8)
liste = []
print(monGraphe.estValide(0,0))
monGraphe.DFS("A1",liste)
print(monGraphe.estValide(0,0))
