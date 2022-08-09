import numpy as np

q=6
numEpocas = 63725

Peso = np.array([113,122,107,98,115,120])
pH = np.array([6.8, 4.7, 5.2, 3.6, 2.9, 4.2])

X = np.vstack((Peso,pH))
Y = np.array([-1,1,-1,-1,1,1])

bias = 1

eta = 0.1

W = np.zeros(3)

e = np.zeros(q)

def ativicao(valor):
    if valor < 0.0:
        return -1
    return 1

for i in range(numEpocas):
    for j in range(q):
        Xb = np.hstack((bias,X[:,j]))
        
        V = np.dot(W, Xb)
        
        Yr = ativicao(V)
        
        e[j] = Y[j] - Yr
        
        W = W + eta*e[j]*Xb
    
print("Vetor de erros (e) = " + str(e))