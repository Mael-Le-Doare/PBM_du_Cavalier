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
        
        #sommetActuel : sommet = self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]]
        #
        #sortie = False
        #if sommetActuel.nom not in listeSortie and not sommetActuel.estVisite:
        #    self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]].estVisite=True
        #    print(listeSortie)
        #    print(sommetActuel)
        #    
        #    for voisins in sommetActuel.sommetAdjacents.keys():
        #        listeSortie.append(sommetActuel.nom)
        #        print(f"je suis en {sommetActuel} je regarde {voisins}")
        #        
        #        if self.DFS(voisins.nom,listeSortie):
        #            sortie = True
        #    
        #            
        #else:
        #    listeSortie.pop()
        #    self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]].estVisite= False
        #print(sortie)
        #return sortie

        sommetActuel : sommet = self.sommets[self.existe(nomSommet)[0]][self.existe(nomSommet)[1]]
        valide = False
        if len(listeSortie) == constantes.board**2 +1:
            return True
        for voisin in sommetActuel.sommetAdjacents.keys():
            if sommetActuel.nom not in listeSortie[:-1]:
                listeSortie.append(voisin.nom)
                if self.DFS(voisin.nom,listeSortie):
                    valide = True
                else:
                    listeSortie.pop()
        return valide
                




        
        



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
    
    def convertionDFS(self, liste : list)->list:
        listeSortie: list = []
        for i in liste:
            listeSortie.append(self.existe(i))
        return listeSortie





