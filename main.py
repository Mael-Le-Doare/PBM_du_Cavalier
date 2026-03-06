import entities
import sommet
import affichage
import constantes
import time


piece = entities.Piece(4,4,constantes.knight)
pl = entities.Plateau(8, 8, piece)
liste = pl.bouger()


for i in liste:
     print(i)


display = affichage.display(constantes.board,"plateau")
display.piece(entities.Position(3,3))
display.passed([(1,2),(2,2)])
display.run()


