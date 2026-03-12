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
        # ✅ Extraire la lettre et le chiffre
        lettre = ord(nomSommet[0]) - ord('A')  # A=0, B=1, ..., H=7
        chiffre = int(nomSommet[1:]) - 1        # 1=0, 2=1, ..., 8=7
    
        # ✅ Vérifier que c'est valide
        if 0 <= lettre < len(self.sommets) and 0 <= chiffre < len(self.sommets):
            return (lettre, chiffre)
    
        return (None, None)
    

    def DFS(self, nomSommet : str, listeSortie : list) -> bool:
        cooSommetActuel : tuple = self.existe(nomSommet)
    
        if cooSommetActuel == (None, None):
            return False
    
        sommetActuel = self.sommets[cooSommetActuel[0]][cooSommetActuel[1]]
    
        if len(listeSortie) == self.ordre:
            return True
        for voisin in sommetActuel.sommetAdjacents:
            cooVoisins = self.existe(voisin.nom)
        
            if not self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite:
                listeSortie.append(voisin.nom)
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = True
            
                if self.DFS(voisin.nom, listeSortie):
                    return True
            
                listeSortie.pop()
                self.sommets[cooVoisins[0]][cooVoisins[1]].estVisite = False
    
        return False


    def convertionDFS(self, liste : list)->list:
        listeSortie: list = []
        for i in liste:
            listeSortie.append(self.existe(i))
        return listeSortie





