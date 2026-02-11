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
    
    def DFS(self, nomSommet : str)->list:
        #renvoie une liste resultant du parcours en largeur du graphe
        listeSortie : list = []
        sommetsATraiter : list = self.sommets.copy()
        sommetActuel : sommet = None
        present : tuple = self.existe(nomSommet)
        while len(sommetsATraiter)!=0:
            if present[0]!=None:
                sommetActuel=self.sommets[present[0]][present[1]]
            listeSortie.append(sommetActuel)
            sommetsATraiter[present[0]].pop(present[1])
            if listeSortie[-1].estVisite!=True:
                present=self.existe(sommetActuel.nom)
                self.sommets[present[0]][present[1]].visite=True
                for voisins in sommetActuel.sommetAdjacents:
                    listeSortie.append(voisins)
                    present=self.existe(voisins.nom)
                    self.sommets[present[0]][present[1]].visite=True
                    sommetsATraiter[present[0]].pop(present[1])
        return listeSortie


                

    

    def existe(self, nomSommet : str)->tuple:
        #methode qui verifie que le sommet est bien present dans le graphe et renvoie ses coordonees
        for i in range(len(self.sommets)):
            for j in range(len(self.sommets)):
                if self.sommets[i][j].nom == nomSommet:
                    return (i,j)
        return (None,None)







monGraphe = Graphe(8)
#monGraphe.afficheSommets()
#print("--------------------------")
#print(monGraphe.sommets[3][4].afficherAdjacents())
#print(monGraphe.ordre)
monGraphe.DFS("A1")
