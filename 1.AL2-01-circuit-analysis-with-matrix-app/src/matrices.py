import numpy as np
import matplotlib.pyplot as pt
from fractions import Fraction
import time

matrix = []
voltageMatrix = []
currentMatrix = []

def createMatrix(index):
    global matrix
    global voltageMatrix
    global currentMatrix

    print(f"Create an Matrix with {index} width")
    matrix = np.zeros((index,index),dtype=float)
    voltageMatrix = np.zeros((index,1),dtype=float)
    currentMatrix = np.zeros((index,1),dtype=float)
    print(matrix)
 

def inputDiagonalNode(index, matrix):

    print("\nEnter the Conductance (1/R): ")
    print("When there are more than one, input with spaces")
    time.sleep(0.3)
    
    for i in range (1,index+1): 
        print(i)
        inputStrConductance = input(f"Conductance (1/R) that connected directly to the node {i} G{i,i}: ")
        # inputIntConductance = 
        # print(inputIntConductance)
        matrix[i-1][i-1] = sum(Fraction(num) for num in inputStrConductance.split())
       
     

    print(matrix)

# Input matrix elemen other than diagonal element
def inputNode(index, matrix, matrixCurrent, matrixVoltage):

    print("\n Enter the other Conductance element")
    print("When there are more than one, input with spaces")

    for i in range (1,index):
        print(f"=== Row {i} ===")
        for j in range (1+i,index+1):
            inputStrConductance = input(f"Conductance that connected directly to node {i} and {j} (G{i}{j} or G{j}{i}): ")
            matrix[i-1][j-1] = -1*sum(Fraction(num) for num in inputStrConductance.split())
            matrix[j-1][i-1] = -1*sum(Fraction(num) for num in inputStrConductance.split())
            print(f"Column {j}")
    print(matrix)

    print("\nNow, Input the current that through node","\n"+
          "If the current that through more than once, input with space and","\n"+
          "Don't forget to add the sign")

    for i in range(1,index+1):
        inputStrCurrent = input(f"Current that through directly to node {i} (I{i}): ")
        matrixCurrent[i-1][0] = sum(float(num) for num in inputStrCurrent.split())
    print(matrixCurrent)

def calculateNode(index, matrix, matrixCurrent, matrixVoltage):
    print("Thank you")
    print("Calculating the voltage")
    print("I = V * G")
    matrixDeterminant = getMatrixDeterminant(matrix)
    cramerMatrix = np.zeros((index,index),dtype =float)
    cramerMatrixCurrent = np.zeros((index,0),dtype=float )
    for i in range (1,index+1):
        cramerMatrix = np.array(matrix)
        print(matrix)
        print(f"Calculate voltage in node {i}")
        for j in range (1,index+1):
            cramerMatrix[j-1][i-1] = matrixCurrent[j-1][0]
            # cramerMatrixCurrent[i-1][0] = matrix[i-1][j-1]
        matrixVoltage[i-1][0] = getMatrixDeterminant(cramerMatrix)/matrixDeterminant
        print(cramerMatrix)
        print(f"The voltage on node {i} is : {matrixVoltage[i-1][0]}V ")



def inputDiagonalMesh(index, matrix):
    print("\nEnter the Resistance (Ω): ")
    print("When there are more than one, input with spaces")
    time.sleep(0.3)
    
    for i in range (1,index+1): 
        print(i)
        inputStrConductance = input(f"Resistor (Ω) passed through the loop {i} (R{i,i}): ")
        # inputIntConductance = 
        # print(inputIntConductance)
        matrix[i-1][i-1] = sum(Fraction(num) for num in inputStrConductance.split())
       

def inputMesh(index, matrix, matrixCurrent, matrixVoltage):
    print("\n Enter the other Resistance (Ω) element")
    print("When there are more than one, input with spaces")

    for i in range (1,index):
        print(f"=== Row {i} ===")
        for j in range (1+i,index+1):
            inputStrConductance = input(f"Resistance (Ω) passed through the loop {i} and {j} (G{i}{j} or G{j}{i}): ")
            matrix[i-1][j-1] = -1*sum(Fraction(num) for num in inputStrConductance.split())
            matrix[j-1][i-1] = -1*sum(Fraction(num) for num in inputStrConductance.split())
            print(f"Column {j}")
    print(matrix)

    print("\nNow, Input the Voltage (V) from battery","\n"+
          "If the current that through more than once, input with space and","\n"+
          "Don't forget to add the sign (When current loop through from plus to minus battery, V is minus)")

    for i in range(1,index+1):
        inputStrVoltage = input(f"Voltage (V) that through directly to mesh/loop {i} (I{i}): ")
        matrixVoltage[i-1][0] = sum(float(num) for num in inputStrVoltage.split())
    print(matrixVoltage)

def calculateMesh(index, matrix, matrixCurrent, matrixVoltage):
    print("Thank you")
    print("Calculating the Current")
    print("V = I*R")
    matrixDeterminant = getMatrixDeterminant(matrix)
    cramerMatrix = np.zeros((index,index),dtype =float)
    cramerMatrixCurrent = np.zeros((index,0),dtype=float )
    for i in range (1,index+1):
        cramerMatrix = np.array(matrix)
        print(matrix)
        print(f"Calculate Current (A) in loop {i}")
        for j in range (1,index+1):
            cramerMatrix[j-1][i-1] = matrixVoltage[j-1][0]
            # cramerMatrixCurrent[i-1][0] = matrix[i-1][j-1]
        matrixCurrent[i-1][0] = getMatrixDeterminant(cramerMatrix)/matrixDeterminant
        print(cramerMatrix)
        print(f"The Current (A) on loop {i} is : {matrixCurrent[i-1][0]}A ")


def getMatrixMinor(matrix, i, j):
    """Hapus baris i dan kolom j dari matrix"""
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)

def getMatrixDeterminant(matrix):
    """Hitung determinan matriks dengan ekspansi kofaktor"""
    n = matrix.shape[0]
    
    # Basis 1x1
    if n == 1:
        return matrix[0,0]
    
    # Basis 2x2 (langsung rumus)
    if n == 2:
        return matrix[0,0]*matrix[1,1] - matrix[0,1]*matrix[1,0]
    
    det = 0
    for j in range(n):
        minor = getMatrixMinor(matrix, 0, j)
        det += ((-1)**j) * matrix[0,j] * getMatrixDeterminant(minor)
    return det


# def getMatrixMinor(i,j,matrix):
#     matrixMinor = np.zeros((len(matrix)-1,len(matrix[0])-1),dtype=float)
    
#     if i==1 and j==1:
#         return pow(-1,i+j) * matrix[i][j]
    
#     for l in range (len(matrix)):
#         if l == i:
#             continue
#         print(f"l = {l}")
#         for m in range (len(matrix)):
#             if m == j:
#                 continue
#             print(f"m = {m}")
#             matrixMinor[l][m] = matrix[l][m]

#     return (pow(-1,i+j) * getMatrixDeterminant(i,j,matrixMinor))

# def getMatrixDeterminant(i,j,matrix):
#     MatrixDeterminant = np.zeros((i,j),dtype=float)

#     return ((matrix)*getMatrixMinor(1,m,matrix) for m in range (matrix))


