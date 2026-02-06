class Plateau:

    vide = 0
    
    def __init__(self, x, y):
        self.matrice = [[self.vide for j in range(x)] for i in range(y)]
        
    def affichage(self):
        for ligne in self.matrice:
            print(ligne)






pl = Plateau(6, 4)
pl.affichage()