import entities
import sommet
import affichage
import constantes


display = affichage.display(constantes.board,"plateau")
display.draw_piece(entities.Position(2,1))
display.run()
display.draw_board()
display.draw_piece(entities.Position(1,2))
