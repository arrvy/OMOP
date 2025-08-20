import numpy as np
import matplotlib.pyplot as pt
import time

matrix = []

def createMatrix(index):
    global matrix
    print(f"Create an Matrix with {index} width")
    matrix = np.zeros((index,index),dtype=float)
    print(matrix)

def inputDiagonalNode(index, matrix):
    print("\nEnter the Conductance (1/R): ")
    print("When there are more than one, series it")
    time.sleep(0.3)
    
    for i in range (1,index+1): 
       print(i)
       matrix[i-1][i-1] = int(input(f"Conductance (1/R) that connected directly to the node {i} G{i,i}: "))
     

    print(matrix)

def inputNode(index, matrix):
    pass

def inputDiagonalMesh(index, matrix):
    pass

def inputMesh(index, matrix):
    pass