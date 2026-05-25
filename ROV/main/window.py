import tkinter

windowCmds = {
    "add": addWindow
}

def windowing(params: list):
    run = windowCmds.get(params[0])
    if run:
        run(params[1:])  # run that function
    else:
        print(f"Error: Unknown command '{params[0]}'")  # unknown comamnd

def addWindow(params: list):
    pass