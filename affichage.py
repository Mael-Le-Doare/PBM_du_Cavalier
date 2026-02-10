import tkinter 

class display:

    



    def draw_board(self):
        for i in range(0,self.board*100,100):
            for j in range(0,self.board*100,100):
                if ((i+j)/100 %2 != 0):
                    self.canvas.create_rectangle(i, j, i+100, j+100, fill = "black")



    def draw_passed(self, liste):
        for i in range(0,self.board):
            for j in range(0,self.board):
                if (i,j) in liste:
                    self.canvas.create_rectangle(i, j, i+100, j+100, fill = "green")


    def draw_piece(self, position):
        x1, y1 = (position.x - 40 + 50), (position.y - 40 + 50)
        x2, y2 = (position.x + 40 + 50), (position.y + 40 + 50)
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue", outline= "black",width=1)

    def __init__(self, board, title):
            self.root = tkinter.Tk()
            self.root.title (title)
            self.canvas = tkinter.Canvas(self.root, width=board*100, height=board*100, bg="white")
            self.canvas.pack()
            self.board = board
            self.draw_board()

    def run(self):
        self.root.update() 

    