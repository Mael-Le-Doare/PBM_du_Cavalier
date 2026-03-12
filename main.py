import affichage
import constantes
import graphe

monGraphe = graphe.Graphe(constantes.board)
liste = ['A1'] 
liste2 = [(0, 0), (1, 2), (2, 4), (3, 6), (5, 7), (7, 6), (6, 4), (5, 6), (7, 7), (6, 5), (5, 3), (7, 4), (6, 6), (5, 4), (7, 5), (6, 7), (5, 5), (4, 7), (3, 5), (2, 7), (4, 6), (3, 4), (2, 6), (4, 5), (3, 7), (2, 5), (1, 7), (0, 5), (1, 3), (3, 2), (4, 4), (6, 3), (5, 1), (7, 2), (6, 0), (5, 2), (7, 1), (5, 0), (6, 2), (4, 3), (3, 1), (1, 0), (2, 2), (0, 1), (2, 0), (4, 1), (3, 3), (1, 4), (0, 2), (2, 3), (4, 2), (6, 1), (4, 0), (2, 1)]

try:
    var = monGraphe.DFS("A1", liste)
except KeyboardInterrupt:
    print("Programme interrompu. Dernière liste en date :")
    print(liste)
    var = False

print(var)
liste=monGraphe.convertionDFS(liste)
print(liste)


display = affichage.display(constantes.board,"plateau", liste)
display.run()

