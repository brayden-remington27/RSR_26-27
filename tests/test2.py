import tkinter as tk

root = tk.Tk()

def initWindow():
    root.title("Tk Example")
    root.configure(background="gray14")
    root.minsize(200, 200)
    root.maxsize(500, 500)
    root.geometry("300x300")
    root.focus_force()

class Node:
    def __init__(self):
        self.ins = []
        self.outs = []
    
    def draw(self):
        pass
    
    def addIn(self, name):
        pass
    
    def addOut(self, name):
        pass
    
    def addProc(self):
        pass
    
    def addSource(self):
        pass
    
canvas = tk.Canvas(root, bg="white")