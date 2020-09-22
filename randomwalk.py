from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
 
def passo_rand(x_0, periodo):
    coef_a = periodo//3
    coef_b = periodo//7
    return ((x_0*coef_a + coef_b)%periodo)
 
def caminhante(eixo, passo, posicao):
    eixos = ['x', 'y', 'z']
    for i in range(len(posicao)):
        if eixos.index(eixo) == i:
            posicao[i].append(posicao[i][-1]+passo)
        else:
            posicao[i].append(posicao[i][-1])
 
    return posicao
 
passos = 1000
caminhadas = 10
periodo = 12345678559098877
val = 0
fig = plt.figure()
ax = fig.gca(projection='3d')
 
for j in range(caminhadas):
    posicao = [[0],[0],[0]] #X, Y, Z
    for i in range(passos):
        print(posicao)
        val = passo_rand(val, periodo)
        if val <= (periodo/6):
            eixo='x'
            passo=+1
            posicao=caminhante(eixo, passo, posicao)
            print('1')
        elif val>(periodo/6) and val<=(2*periodo/6):
            eixo='x'
            passo=-1
            posicao=caminhante(eixo, passo, posicao)
            print('2')
        elif val>(2*periodo/6) and val<=(3*periodo/6):
            eixo='y'
            passo=+1
            posicao=caminhante(eixo, passo, posicao)
            print('3')
        elif val>(3*periodo/6) and val<=(4*periodo/6):
            eixo='y'
            passo=-1
            posicao=caminhante(eixo, passo, posicao)
            print('4')
        elif val>(4*periodo/6) and val<=(5*periodo/6):
            eixo='z'
            passo=+1
            posicao=caminhante(eixo, passo, posicao)
            print('5')
        elif val>(5*periodo/6) and val<=(6*periodo/6):
            eixo='z'
            passo=-1
            posicao=caminhante(eixo, passo, posicao)
            print('6')
    ax.plot(posicao[0], posicao[1], posicao[2], label=f'Caminhada {j+1}')
 
ax.legend()
plt.show()