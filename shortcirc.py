# Códigos do artigo: 
# Short Circuiting no Python 3: Fechando curtos-circuitos em seus códigos.

# Função para teste lógico de valores
def teste_tf(valor):
    if valor:
        print(f"{valor} é avaliado como verdadeiro.")
    else:
        print(f"{valor} é avaliado como falso.")


# Declaração de valores para teste
valores = [
    None, [], (), {}, set(), "", range(0), [1,2], (3,4), set([5,6]), {'a','a'},
    ' ', 'a', 'A', 1, 2, 1.2, 3.2e3
]

# Teste dos valores
for i in valores:
    teste_tf(i)