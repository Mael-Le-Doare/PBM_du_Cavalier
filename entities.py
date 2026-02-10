import constantes

class Position: #c'est la classe qui gère la position
    
    def __init__(self, x = 0, y = 0): #on initialise    
        self.x = x
        self.y = y 

    def __add__(self, other):
        p = Position()
        p.x = other.x + self.x
        p.y = other.y + self.y
        return p 
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)

    def getMat(self,mat):
        return mat[self.x][self.y]

    def setMat(self, mat, val):
        mat[self.x][self.y] = val

class Plateau: #c'est la classe pour le plateau
    vide = 0

    def __init__(self, x, y, piece):
        self.matrice = [[self.vide for j in range(x)] for i in range(y)]
        self.piece = piece
        
    def affichage(self):
        for ligne in self.matrice:
            print(ligne)
        self.piece.affichage()

    def bouger(self):
        liste = []
        for move in self.piece.movement():
            if move.x >=0 and move.x <= 7 \
                and move.y >=0 and move.y <= 7 \
                and move.getMat(self.matrice) == 0:
                liste.append(move)
        return liste
            
    def accept(self, x, y):
        pos = Position(x,y)
        if pos in self.bouger():
            self.piece.position()
            return True
        return False

class Piece: #C'est la classe pour la piece
    relative_movements = []

    def __init__(self, x, y, mouvements):
        for pos in mouvements:
            self.relative_movements.append(Position(*pos))
        self.position = Position(x, y)
        

    def movement(self):
        liste = []
        for i in self.relative_movements:
            liste.append(self.position + i)
        return liste
    
    def affichage(self):    
        print(self.relative_movements)
        print(self.position)
