import re
from window import *
from cmdLine import *

running = True

def quit():
    running = False

functions = {  # list of all possible commands and the functions that they activate
    "q": quit,
    "echo": echoing,
    "window": windowing
}




# TODO: have it so that this live updates a script file of all the commands to be called up whenever

while running:
    inp = input("[Surface@ROV] > ").strip()  # remove leading and trailing whitespace
    if not inp:
        continue  # continue if no input
    
    # split the first from the rest
    tokens = inp.split(maxsplit=1)
    cmd = tokens[0]  # the first is the command
    params = tokens[1].split() if len(tokens) > 1 else None
    
    #print(inp, "///", cmd, ":", params)
    
    
    
    # from the function list get the one that responds to the user inputted command
    run = functions.get(cmd)  
    if run:
        run(params)  # run that function
    else:
        print(f"Error: Unknown command '{cmd}'")  # unknown comamnd
