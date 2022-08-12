import numpy as np

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

numEpocas = 2
q = 50

X1 = np.random.normal(10,1,q)
X2 = np.random.normal(-10,1,q)
X = np.hstack((X1,X2))
Y = np.array([1,-1])
Y = np.repeat(Y,q)

X,Y = unison_shuffled_copies(X,Y)

W = np.zeros(2)
e = np.ones(q*2)
bias = 1
eta = 0.1

for j in range(numEpocas):
  for i in range(q*2):
    Xb = np.hstack((bias,X[i]))
    V = np.dot(W,Xb)
    Yr = np.sign(V)
    e[i] = Y[i] - Yr
    W = W + eta*e[i]*Xb

print("O vetor de erros (e) = " + str(e))
