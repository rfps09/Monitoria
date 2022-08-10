import numpy as np

numEpocas = 4
q = 4

X1 = np.array([0,0,1,1])
X2 = np.array([0,1,0,1])
X = np.vstack((X1,X2))
Y = np.array([0,1,1,1])
W = np.zeros(3)
e = np.zeros(q)
bias = 1
eta = 0.1

for j in range(numEpocas):
    for i in range(q):
        Xb = np.hstack((bias, X[:,i]))
        V = np.dot(W,Xb)
        Yr = np.heaviside(V,0)
        e[i] = Y[i] - Yr
        W = W + eta*e[i]*Xb

print("O vetor de erros (e) = " + str(e))