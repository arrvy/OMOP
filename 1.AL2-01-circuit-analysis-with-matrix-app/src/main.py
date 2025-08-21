import os,time
import matrices

# Main Function
def main():
    opening()
    menuSystem()
    ending()
    ending()
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
    quitInput = 'Y'

    while quitInput !='N' and quitInput !='n' :
        chooseInput = 0
        if quitInput == 'Y' or quitInput == 'y':
            print("="*100)
            print("")
            print("="*100)
        if quitInput != 'Y' and quitInput != 'y':
            quitInput = input("Do you want to calculate again? : [Y]es for again, [N]o for quit [Y/N][y/n]: ")
            continue
        while chooseInput!='1' and chooseInput!='2':
            print("Select the Analysis Method:")
            print("1. Nodal Analysis")
            print("2. Mesh Analysis")
            chooseInput = input("Select the method [1/2]: ")
            match chooseInput:
                case '1':
                    nodalMethod()
                case '2':
                    meshMethod()
                case _:
                    print("\nEnter the correct value, you fucking moron\n\n")

        quitInput = input("Do you want to calculate again? : [Y]es for again, [N]o for quit [Y/N][y/n]: ")
        if quitInput != 'Y' and quitInput !='y' and quitInput != "N" and quitInput !="n" :
            print("Input the fucking correct option")


# quitInput = input("Do you want to calculate again? : [Y]es for again, [N]o for quit [Y/N][y/n]: ")
#         if quitInput != 'Y' and quitInput !='y' and quitInput != "N" and quitInput !="n" :
#             print("Input the fucking correct option")

def ending():
    ending = "THANK YOU FOR USING CIRCUIT ANALYSIS WITH MATRICES"
    ending2 = "OMOP Projects"
    ending3 = "By Tatizen Group"
    spacing = (100-len(ending))//2 # Centering word
    spacing2 = (100-len(ending2))//2
    spacing3 = (100-len(ending3))//2        
    print("="*100)
    print(" "*spacing,ending)
    print(" "*spacing2,ending2)
    print(" "*spacing3,ending3)
    print("="*100)
    
        

# Nodal mode
def nodalMethod():
    node = 0
    print("\nChoose 1 Reference Node (arbritary)")
    node = int(input("How many Nodes (except nodes refence) in the circuit?: "))
    matrices.createMatrix(node)
    matrices.inputDiagonalNode(node, matrices.matrix)
    matrices.inputNode(node,matrices.matrix,matrices.currentMatrix,matrices.voltageMatrix)
    matrices.calculateNode(node,matrices.matrix,matrices.currentMatrix,matrices.voltageMatrix)
    

# Mesh modex
def meshMethod():
    mesh = 0
    print("Choose Loop Reference (all clockwise for recommendation) and")
    print("When current through battery from plus to minus, voltage is minus ()")
    mesh = int(input("How many Mesh in the circuit?: "))
    matrices.createMatrix(mesh)
    matrices.inputDiagonalMesh(mesh, matrices.matrix)
    matrices.inputMesh(mesh,matrices.matrix,matrices.currentMatrix,matrices.voltageMatrix)
    matrices.calculateMesh(mesh,matrices.matrix,matrices.currentMatrix,matrices.voltageMatrix)


# Start of the code
if __name__ == '__main__':
    print("Program Oppened")
    time.sleep(0.5)
    _ = os.system("cls")
    main()