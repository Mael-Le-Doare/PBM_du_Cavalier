import tkinter 
import entities

class display:

    def draw(self):
        self.canvas.delete("all") 
        self.draw_b()
        self.draw_pa()
        if self.count < len(self.path) :
            self.draw_p()
        self.draw_trajet()  

    def update(self):
        if self.count < len(self.path) :
            self.count += 1 
            self.liste.append(self.position)
            self.position = entities.Position(*self.path[self.count])
        self.draw()

    def draw_b(self):
        self.canvas.create_rectangle(0, 0, self.board*100, self.board*100, fill = "white")
        for i in range(0,self.board*100,100):
            for j in range(0,self.board*100,100):
                if ((i+j)//100 % 2 != 0):
                    self.canvas.create_rectangle(i, j, i+100, j+100, fill = "black")

    def draw_pa(self):
        for idx, position in enumerate(self.liste):
            self.canvas.create_rectangle(
                position.x*100+30, position.y*100+30,
                (position.x+1)*100-30, (position.y+1)*100-30, fill="green"
            )
            self.canvas.create_text(
                position.x*100+50, position.y*100+50,
                text=str(idx+1), font=("Arial", 16, "bold"), fill="white"
            )

    def draw_trajet(self):
        if len(self.liste) > 1:
            points = [
                (pos.x*100+50, pos.y*100+50)
                for pos in self.liste
            ]
            for i in range(len(points)-1):
                self.canvas.create_line(
                    points[i][0], points[i][1],
                    points[i+1][0], points[i+1][1],
                    fill="red", width=3
                )

    def draw_p(self):
        if self.count < len(self.path):
            x1, y1 = (self.position.x*100 - 40 + 50), (self.position.y*100  - 40 + 50)
            x2, y2 = (self.position.x*100  + 40 + 50), (self.position.y*100  + 40 + 50)
            self.canvas.create_oval(x1, y1, x2, y2, fill="blue", outline="black", width=1)


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
        self.draw()
        
    def run(self):
        self.root.mainloop() 
