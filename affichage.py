import tkinter 

class display:

    def __init__(self, board, title):
        root= tkinter.Tk()
        root.title (title)
        self.canvas=tkinter.Canvas(root, width=board*100, height=board*100, bg="white")
        self.canvas.pack()
        self.board = board
        self.draw_board()

        root.mainloop()



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
        x1, y1 = (position.x - 40), (position.y - 40)
        x2, y2 = (position.x + 40), (position.y + 40)
        self.canvas.create_oval(x1, y1, x2, y2, fill="blue")



