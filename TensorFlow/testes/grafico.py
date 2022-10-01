import numpy as np
import matplotlib.pyplot as plt 

numEpocas = 4
q = 4

X1 = np.array([0,0,1,1])
X2 = np.array([0,1,0,1])
X = np.vstack((X1,X2))
Y = np.array([0,1,1,1])
W = np.array([0,1,-1])
e = np.zeros(q)
bias = 1
eta = 0.8

def draw_decision_boundary(a,b,c):
    space = np.linspace(-10,10,100)

    linear = space*(a / (-b) ) +  c/ (-b)

    points_x_green = [1,1,0]
    points_y_green = [1,0,1]

    points_x_blue = [0]
    points_y_blue = [0]

    plt.plot(space,linear,'r')
    plt.plot(points_x_green,points_y_green,'o',markerfacecolor="green",markeredgecolor="green")
    plt.plot(points_x_blue,points_y_blue,'o',markerfacecolor="blue",markeredgecolor="blue")
    plt.show()

def funcaoDeAtivicao(valor):
    if valor < 0.0:
        return 0
    return 1

for j in range(numEpocas):
    for i in range(q):
        Xb = np.hstack((bias, X[:,i]))
        V = np.dot(W,Xb)
        Yr = funcaoDeAtivicao(V)
        e[i] = Y[i] - Yr
        W = W + eta*e[i]*Xb
        draw_decision_boundary(W[1],W[2],W[0])

print("O vetor de erros (e) = " + str(e))