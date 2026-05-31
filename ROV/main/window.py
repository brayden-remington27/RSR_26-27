import tkinter as tk
from cmdLine import quit

# RUN WHEN IMPORTED
windows = []  # root = [0]

def addWindow(params: list):
    if len(params) >= 1:
        name = params[0]
        size = params[1]  # widthxheight
    elif len(params) >= 2:
        name = params[0]
    else:
        print("! not enugh arguments !")
        return
    
    index = len(windows)
    if index == 0:
        windows.append(tk.Tk())
        windows[index].protocol("WM_DELETE_WINDOW", quit(params))  # this is so stupid
    else:
        windows.append(tk.Toplevel(windows[0]))
    windows[index].title(name)
    windows[index].geometry(size)
    #windows[index].attributes('-topmost', True)  # bring to the front
    windows[index].focus_force()
        
def help(params: list):
    print("Avalible commands:")
    print("------------------")
    print("add: name size(widthxheight)")
    
windowCmds = {
    "add": addWindow,
    "help": help
}

def windowing(params: list):
    run = windowCmds.get(params[0])
    if run:
        run(params[1:])  # run that function
    else:
        print(f"Error: Unknown command '{params[0]}', use 'window help' for more information")  # unknown comamnd

from env import quit