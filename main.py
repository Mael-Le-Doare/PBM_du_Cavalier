import affichage
import constantes
import graphe

monGraphe = graphe.Graphe(constantes.board)
liste = []
monGraphe.DFS("A1",liste)

print(liste)

display = affichage.display(constantes.board,"plateau", liste)
display.run()


