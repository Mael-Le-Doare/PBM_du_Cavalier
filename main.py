import entities
import sommet
import affichage
import constantes


piece = entities.Piece(0,0,constantes.knight)
pl = entities.Plateau(6, 4, piece)
liste = pl.bouger()



display = affichage.display(constantes.board,"plateau")
display.draw_piece(entities.Position(2,1))
display.run()
display.draw_board()
display.draw_piece(entities.Position(1,2))
