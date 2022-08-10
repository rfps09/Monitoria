import numpy as np

numEpocas = 3
q = 2

X = np.array([0,1])
Y = np.array([1,0])
W = np.zeros(2)
e = np.zeros(2)
bias = 1
eta = 0.1

for j in range(numEpocas):
    for i in range(q):
        Xb = np.hstack((bias, X[i]))
        V = np.dot(W, Xb)
        Yr = np.heaviside(V,0)
        e[i] = Y[i] - Yr
        W = W + eta*e[i]*Xb
        
print("O vetor de erros (e) = " +  str(e))