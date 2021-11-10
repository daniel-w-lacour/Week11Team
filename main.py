import numpy as np
A = np.array([[0,1,2,3],[4,5,6,7],[8,9, 10, 11]])
print("A =", A, "\n")
B = np.array([[0,1],[2,3],[4,5],[6,7]])
print("B =", B, "\n")
C = np.array([[0,1,2],[3,4,5]])
print("C =", C, "\n")
D = np.linalg.multi_dot([A,B,C])
print("D =", D, "\n")
E = np.transpose(D)
print("D^T =", D, "\n")
F = np.sqrt(D)/2
print("E =", F)

