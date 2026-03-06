import tkinter 
import entities

class display:


    def draw(self):
        self.draw_b()
        self.draw_pa()
        self.draw_p()
        
    def update(self):
        self.count += 1 
        self.draw()
        self.liste.append(self.position)
        self.position = entities.Position(*self.path[self.count])

    def draw_b(self):
        self.canvas.create_rectangle(0, 0, self.board*100, self.board*100, fill = "white")
        for i in range(0,self.board*100,100):
            for j in range(0,self.board*100,100):
                if ((i+j)/100 %2 != 0):
                    self.canvas.create_rectangle(i, j, i+100, j+100, fill = "black")

    def draw_pa(self):
        for position in self.liste:
            self.canvas.create_rectangle(position.x*100+30, position.y*100+30, (position.x+1)*100-30,
                                          (position.y+1)*100-30, fill = "green")
            #label = self.root.Label(self.root,text=str(self.count))
            #label.place(x=position.x-40,y=position.y-40)



        #for i in range(0,self.board):
        #    for j in range(0,self.board):
        #        if (i,j) in self.liste:
        #            self.canvas.create_rectangle(i*100+30, j*100+30, (i+1)*100-30, (j+1)*100-30, fill = "green")

    def draw_p(self):
        x1, y1 = (self.position.x*100 - 40 + 50), (self.position.y*100  - 40 + 50)
        x2, y2 = (self.position.x*100  + 40 + 50), (self.position.y*100  + 40 + 50)
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", outline= "black",width=1)

    def __init__(self, board, title, path):
            self.root = tkinter.Tk()
            self.root.title (title)
            self.canvas = tkinter.Canvas(self.root, width=board*100, height=board*100+50, bg="white")
            self.canvas.pack()
            self.b = tkinter.Button(self.root, text = "mouvement suivant", command=self.update)
            self.b.pack() 
            self.liste = []
            self.position = entities.Position()
            self.board = board
            self.path = path
            self.count = 0

    def run(self):
        self.root.mainloop() 

