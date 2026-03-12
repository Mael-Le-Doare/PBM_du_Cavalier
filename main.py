import affichage
import constantes
import graphe


#on demande la taille du plateau
constantes.board = int(input("Veuillez renseigner la taille du plateau : ").upper())

#on definit notre objet graphe
monGraphe = graphe.Graphe(constantes.board)
#on definit la liste qui contiendra nos positions
liste = [] 

#on reinitianalise tout les sommets à esVisite = False
for liste in monGraphe.sommets:
    for sommet in liste:
        sommet.estVisite = False

#on demande la case au clavier tant qu'elle n'est pas valide
depart = input("Veuillez renseigner la case de depart : ").upper()
while monGraphe.existe(depart)[0]==None:
    print("Case invalide")
    depart = input("Veuillez renseigner la case de depart : ").upper()

#on demande si l'on souhaite chercher un cycle
cycle = input("Voulez chercher un chemin qui effectue un cycle ? (O/N): ").upper()
while cycle!="O" and cycle!="N":
    print("Caractère inconnu")
    depart = input("Voulez vous chercher un chemin qui effectue un cycle ? (O/N): ").upper()
#on met la case de depart comme visitee
coords_depart = monGraphe.existe(depart)
x, y = coords_depart
monGraphe.sommets[x][y].estVisite = True

#on initianalise la liste de parcours avec le point de départ
liste = [depart]

#on lance le  DFS en fonction de la recherche de cycle ou non
if cycle=="N":
    var = monGraphe.DFS(depart, liste)
else:
    var = monGraphe.DFSCycle(depart,depart,liste)

liste=monGraphe.convertionDFS(liste)

# si la longueur de la liste n'est pas égalle à la taille du plateau, alors il n'y a pas de solution
if cycle=="N":
    if len(liste)!=constantes.board**2:
        print(f"Le tour du cavalier est impossible en partant de {depart} !")
    else:
        print(f"Le tour du cavalier est possible en partant de {depart} !")
else:
    if len(liste)!=constantes.board**2:
        print(f"Le tour du cavalier avec cycle est impossible en partant de {depart} !")
    else:
        print(f"Le tour du cavalier avec cycle est possible en partant de {depart} !")
        liste.append(monGraphe.existe(depart))
        retourDebut : bool =True

#affichage graphique de notre parcours du cavalier
display = affichage.display(constantes.board,"plateau", liste)
display.run()


