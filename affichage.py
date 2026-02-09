import tkinter 

def draw_samples (canvas):
    canvas.create_rectangle ((100, 100), (600, 600),  
                             fill="cyan", outline="blue", width=5)

    canvas.create_oval ((100, 100), (600, 600), 
                        fill="pink", outline="red", width=3)

    canvas.create_line ((100, 100), (500, 200),(600, 600), 
                        fill="gray", width=3, dash=(8,4))

    canvas.create_line ((100, 100), (500, 200), (600, 600), 
                        fill="black", width=5, smooth=True,
                        arrow="last", arrowshape=(30,45,15))
 
    canvas.create_text (600, 100, text= "Hello\nEverybody",
                        fill= "black", font= ("courier", 30, "bold italic"),
                        anchor="center", justify= "center")

root= tkinter.Tk()
root.title ("demo")
canvas=tkinter.Canvas(root, width=800, height=800, bg="white")
canvas.pack()


def draw_vertex (canvas, center, radius, label):
    canvas.create_oval ((center[0]-radius, center[1]-radius), (center[0]+radius, center[1]+radius),
                        fill="yellow", outline="blue", width=1)

    canvas.create_text (center, text= label,
                        fill= "black",
                        anchor="center", justify= "center")

draw_vertex (canvas, (400, 300), 15, "A")
draw_vertex (canvas, (200, 500), 15, "B")
draw_vertex (canvas, (500, 500), 15, "C")

def draw_straight_arc (canvas, start, end, label):
    canvas.create_line ((100, 100), (500, 200), (600, 600), 
                        fill="green", width=1, smooth=True,
                        arrow="last", arrowshape=(30,45,15))

draw_straight_arc (canvas, (400, 300), (200, 500), "10")
draw_straight_arc (canvas, (200, 500), (500, 500), "20")
draw_straight_arc (canvas, (500, 500), (400, 300), "30")


root.mainloop()
