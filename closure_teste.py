import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# Implementa o modelo matemático padrão.
def modelo(param, vec_x, vec_y):
    """ 
     Recebe uma lista ou tupla (param) com 8 parâmetros para serem utilizados 
     no modelo e dois vetores (vec_x e vec_y) para serem utilizados como 
     variáveis para o modelo e retorna o vetor f(x,y).

     A função foi definida aleatoriamente.
    """

    return (
            param[0]*vec_x + param[1]*vec_y + param[2]*(vec_x+vec_y) + \
            param[3]*vec_y*vec_x + param[4]*(vec_x-vec_y)
    ) 

# Implementa o modelo matemático padrão inclausurado .
# Note a ausência dos vetores
def cloistered_model(param):
    """ 
     Recebe uma lista ou tupla (param) com 8 parâmetros para serem utilizados 
     no enclausuramento do modelo.
    """

    def func(vec_x, vec_y):
        return(
            param[0]*vec_x + param[1]*vec_y + param[2]*(vec_x+vec_y) + \
            param[3]*vec_y*vec_x + param[4]*(vec_x-vec_y)
        )

    return func

def vecs_x_y(raio_maior, raio_menor, d_theta):
    """
     Recebe dois valores de raio para o retorno dos vetores X e Y que serão 
     aplicados às funções model e cloistered_model. Para este caso, foi 
     selecionado um hipotrocoide como curva X,Y passada ao modelo.

     O parâmetro d_theta é a fração de theta em radianos para a discretização
     da variação de theta na composição do hipotrocoide.
    """

    theta = np.arange(0,6*np.pi,d_theta)
    
    xis = (raio_maior - raio_menor)*np.cos(theta) + \
    raio_maior*np.cos((raio_maior - raio_menor)/raio_menor * theta)
    
    yps =  (raio_maior - raio_menor)*np.sin(theta) - \
    raio_maior*np.sin((raio_maior - raio_menor)/raio_menor * theta)

    return xis, yps

def plotter(param, xis, yps):


    fig = plt.figure(figsize=plt.figaspect(0.5))
    ax = fig.add_subplot(1,2,1)
    ax.plot(xis, yps)
    ax.grid()

    # Exibe o comportamento do modelo para o primeiro vetor da array
    ax = fig.add_subplot(1,2,2, projection="3d")

    for i in param[:5]:
        ax.plot(xis, yps, modelo(i, xis, yps))
    
    plt.show()


if __name__ == "__main__":


    # Define parâmetros aleatórios para o modelo, neste caso uma array com 
    # 100 linhas contendo vetores de comprimento 5
    param = 20*np.random.random_sample([20,5])-10

    # Exibe a curva X,Y formada pelos vetores retornados pela função vec_x_y
    xis, yps = vecs_x_y(5,3, 1e-6)

    # Discomentar plotter para obter os gráficos, neste caso, diminuir a 
    # discretização no terceiro parâmetro da chamada à vecs_x_y()
    # plotter(param, xis, yps)

    # Opera o somatório do modelo para os 100 conjunots de parâmetros passados 
    # para a função e armazena em um vetor numpy.
    # o código é declarado como string para uso do módulo timeit


    # Operando com o modelo origianal

    start_time = timer()
    sum_full_model = np.array([modelo(i, xis, yps) for i in param])
    end_time = timer()
    print(
        "O tempo de execução para o modelo completo foi de " +\
        f"{end_time - start_time} segundos."
    )

    # Operando com o modelo enclausurado
    start_time = timer()
    closure_model = np.array([cloistered_model(i) for i in param])
    end_time = timer()

    print(
        "O tempo de execução para o modelo enclausurado foi de " +\
        f"{end_time - start_time} segundos."
    )

