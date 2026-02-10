import entities
import sommet
import affichage
import constantes


piece = entities.Piece(4,4,constantes.knight)
pl = entities.Plateau(8, 8, piece)
liste = pl.bouger()


for i in liste:
     print(i)


display = affichage.display(constantes.board,"plateau")
display.draw_piece(entities.Position(2,1))
display.run()
display.draw_board()
display.draw_piece(entities.Position(1,2))
