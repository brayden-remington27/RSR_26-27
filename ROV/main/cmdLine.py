import config

def echoing(params: list):
    for word in params:
        print(word, "", end="")
    if params: print()

def quit(params: list):
    config.running = False