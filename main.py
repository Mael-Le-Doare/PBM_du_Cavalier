import affichage
import constantes
import graphe

monGraphe = graphe.Graphe(constantes.board)
liste = [] 
var = monGraphe.DFS("A1",liste)
print(var)
liste=monGraphe.convertionDFS(liste)
print(liste)


display = affichage.display(constantes.board,"plateau", liste)
display.run()

