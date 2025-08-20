import os,time
import matrices

# Main Function
def main():
    opening()
    menuSystem()

# Opening CLI
def opening():
    opening = "WELCOME TO CIRCUIT ANALSYSIS WITH MATRICES"
    spacing = (100-len(opening))//2 # Centering word
    print("="*100)
    print(" "*spacing,opening)
    print("="*100)

# Code for user input mode and validation
def menuSystem():
    chooseInput = 0
    while chooseInput!=1 and chooseInput!=2:
        print("Select the Analysis Method:")
        print("1. Nodal Analysis")
        print("2. Mesh Analysis")
        chooseInput = int(input("Select the method [1/2]: "))
        match chooseInput:
            case 1:
                nodalMethod()
            case 2:
                meshMethod()
            case _:
                print("\nEnter the correct value, you fucking moron\n\n")

# Nodal mode
def nodalMethod():
    node = 0
    print("\nChoose 1 Reference Node (arbritary)")
    node = int(input("How many Nodes (except nodes refence) in the circuit?: "))
    matrices.createMatrix(node)
    matrices.inputDiagonalNode(node, matrices.matrix)
    matrices.inputNode(node,matrices.matrix)
    

# Mesh modex
def meshMethod():
    mesh = 0
    mesh = int(input("How many Mesh in the circuit?: "))
    matrices.createMatrix(mesh)


# Start of the code
if __name__ == '__main__':
    print("Program Oppened")
    time.sleep(0.5)
    _ = os.system("cls")
    main()