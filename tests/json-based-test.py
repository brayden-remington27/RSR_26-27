import json

file = 'tests/nodes.json'

nodes = {}
with open(file, 'r') as json_file:
    nodes = json.load(json_file)

while True:
    cmd = input("<cmd> ")
    if cmd == "add-node":
        name = input("name: ")
        nin = int(input("how many inputs: "))
        nout = int(input("how many outputs: "))
        
        # runs through the menu for the number of inputs and outputs selected
        ins = [{"name": input("name of input: "), 
                "type": input("data type of input: "), 
                "source": input("source to input ([nodeName, outName], [c] for custom): ")} 
                for i in range(nin)]
        
        outs = [{"name": input("name of output: "), 
                "type": input("data type of output: ")} 
                for i in range(nout)]
        
        nodes[name] = {
            "inputs": ins,
            "outputs": outs
            #TODO: add more onto this for graphical stuff
        }
    elif cmd == "del-node":
        name = input("name: ")
        del nodes[name]
    
    #TODO: it might be more effective to store the ins/outs as ins/outs: {name: type, name, type, …}, but that removes consistant ordering from the display idk
    #TODO: a lot of repeated code, restructure as functions
    elif cmd == "add-in":
        name = input("node with input: ")
        nodes[name]["inputs"].append({"name": input("name of input: "), 
                "type": input("data type of input: "), 
                "source": input("source to input ([nodeName, out#], [c] for custom): ")})
    elif cmd == "del-in":
        name = input("node with input: ")
        inpName = input("input name: ")
        # basically replaces the list cuz I can't use pop or remove with the name inside a dictionary
        nodes[name]["inputs"] = [inp for inp in nodes[name]["inputs"] if inp["name"] != inpName]
    
    elif cmd == "add-out":
        name = input("node with output: ")
        nodes[name]["outputs"].append({"name": input("name of output: "), 
                "type": input("data type of output: ")})
    elif cmd == "del-out":
        name = input("node with output: ")
        inpName = input("output name: ")
        # basically replaces the list cuz I can't use pop or remove with the name inside a dictionary
        nodes[name]["outputs"] = [inp for inp in nodes[name]["outputs"] if inp["name"] != inpName]
    
    #TODO: reorder-in/out function, to move an in/out to a different spot in the list of ins/outs
    
    
    elif cmd == "print":
        with open(file, "r") as json_file:
            str = json.load(json_file)
        print(json.dumps(str, indent=4))
        
    elif cmd == "q":
        break
    
    else:
        print("unknown command, try again")
        
        
        
    # push everything into an output folder
    with open(file, "w") as json_file:
        json.dump(nodes, json_file, indent=4)