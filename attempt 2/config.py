import pygame, json, os

## WINDOW ##
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (30,40,50)

## TEXT ##
FONT = pygame.font.SysFont("Arial", 16, bold=True)
ANTIALIAS = True
TEXT_COLOR = (255,255,255)
TEXT_BUFFER = (20,20)  # TOP/BOTTOM

## NODES ##
NODE_BORDER_WIDTH = 3
NODE_BORDER_RADIUS = 4
NODE_BORDER_COLOR_OFFSET = 30

## WIRES ##
WIRE_COLOR = (255,255,255)
WIRE_WIDTH = 1


## PROJECT ##
SAVE_FILE = "attempt 2/save.json"

#------------------------------------------#
#                 FUNCTIONS                #
#------------------------------------------#

def save(nodes: dict):  # should be able to extrapolate everything from the nodes
    nodesSave = {
        "nodes": [
            {
                "ID": i,
                "title": nodes[i].title,
                "box": tuple(nodes[i].box),
                "color": nodes[i].color,
                "nIO": nodes[i].nIO,
                # TODO: add some way to save connections for lines later on
            }
        for i in range(len(nodes))
        ]
    }
    
    with open(SAVE_FILE, "w", encoding="utf-8") as file:  # push to the file
        json.dump(nodesSave, file, indent=4)
    
    print("Saved!")

def load():
    from elements import Node
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    
    nodes = [
            Node(i["title"], (i["box"][0], i["box"][1]), i["color"], i["nIO"])
        for i in data["nodes"]
        ]
    
    return {
        "nodes": nodes,
        "lines": {}
    }