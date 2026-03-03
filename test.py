import entities
import sommet
import affichage
import constantes
import time
import tkinter



class display:


    def draw(self):
        print("runing")
        print(self.changed)
        if self.changed:
            print("changed")
            self.draw_b()
            self.draw_pa()
            self.draw_p()
            self.changed = False

        self.root.after(50, self.draw) 
        
    def passed(self, liste):
        self.liste = liste
        self.changed = True


    def piece(self, position):
        self.position = position
        self.changed = True


    def draw_b(self):
        for i in range(0,self.board*100,100):
            for j in range(0,self.board*100,100):
                if ((i+j)/100 %2 != 0):
                    self.canvas.create_rectangle(i, j, i+100, j+100, fill = "black")

    def draw_pa(self):
        for i in range(0,self.board):
            for j in range(0,self.board):
                if (i,j) in self.liste:
                    self.canvas.create_rectangle(i*100+30, j*100+30, (i+1)*100-30, (j+1)*100-30, fill = "green")

    def draw_p(self):
        x1, y1 = (self.position.x*100 - 40 + 50), (self.position.y*100  - 40 + 50)
        x2, y2 = (self.position.x*100  + 40 + 50), (self.position.y*100  + 40 + 50)
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", outline= "black",width=1)

    def __init__(self, board, title):
            self.root = tkinter.Tk()
            self.root.title (title)
            self.canvas = tkinter.Canvas(self.root, width=board*100, height=board*100, bg="white")
            self.canvas.pack()
            self.board = board
            self.draw_b()

    def run(self):
        self.changed = True
        self.root.after(50, self.draw) 
        self.root.mainloop() 



piece = entities.Piece(4,4,constantes.knight)
pl = entities.Plateau(8, 8, piece)
liste = pl.bouger()


for i in liste:
    print(i)


display = affichage.display(constantes.board,"plateau")
display.piece(entities.Position(3,3))
display.passed([(1,2),(2,2)])
display.run()


display.piece(entities.Position(3,4))
display.passed([(1,2),(2,2),(3,3)])