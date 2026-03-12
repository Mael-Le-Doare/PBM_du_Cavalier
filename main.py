import affichage
import constantes
import graphe

monGraphe = graphe.Graphe(constantes.board)
liste = [] 

# Réinitialiser tous les sommets
for i in monGraphe.sommets:
    for j in i:
        j.estVisite = False

# Marquer le sommet de départ comme visité
coords_depart = monGraphe.existe("A1")
x, y = coords_depart
monGraphe.sommets[x][y].estVisite = True

# Initialiser la liste avec le point de départ
liste = ["A1"]

# Lancer DFS
var = monGraphe.DFS("A1", liste)
print(var)
liste=monGraphe.convertionDFS(liste)
print(liste)


display = affichage.display(constantes.board,"plateau", liste)
display.run()

