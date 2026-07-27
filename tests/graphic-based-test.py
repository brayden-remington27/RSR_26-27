import tkinter as tk

root = tk.Tk()

def initWindow():
    root.title("Tk Example")
    root.configure(background="gray14")
    root.minsize(400, 400)
    root.maxsize(800, 1000)
    root.geometry("300x300")
    root.focus_force()

class Node:
    def __init__(self, name, pos=(100, 100)):
        self.ins = []
        self.outs = []
        
        
        # Set body to the size of Title Name Text
        self.name = name
        
        #TODO: do automatically updating margins for the title text
        self.title = canvas.create_text(pos[0], pos[1], text=self.name, font=("SF Mono", 16), fill="gray")
        root.update_idletasks()  # ensure the geometry is fetchable
        textBounds = canvas.bbox(self.title)
        # titleWidth = textBounds[2] - textBounds[0]
        self.body = canvas.create_rectangle(textBounds[0]-10, textBounds[1]-10, textBounds[2]+10, textBounds[3]+10, fill="blue", outline="black", width=3)
        canvas.tag_raise(self.title)
        
        canvas.itemconfig(self.title, state="hidden")
        canvas.itemconfig(self.body, state="hidden")
    
    def draw(self):
        canvas.itemconfig(self.title, state="normal")
        canvas.itemconfig(self.body, state="normal")
    
    def addIn(self, name):
        self.ins.append(name)
    
    def addOut(self, name):
        pass
    
    def addProc(self):
        pass
    
    def addSource(self):
        pass

initWindow()
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)  # automatically sets it to resize with the window

node1 = Node("Inputs")
#for i in range(10): node1.addIn("in"+i)

root.mainloop()