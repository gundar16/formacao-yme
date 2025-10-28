# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Função que gera uma lista com os x primeiros números de Fibonacci
def list_generator(x):
    lista = []
    for i in range(x):
        lista.append(fibonacci(i))
    return lista

# Função que devolve um dicionário com estatísticas da lista
def estatisticas(lista):
    return {
        "tamanho": len(lista),
        "somatorio": sum(lista),
        "maximo": max(lista) if lista else None,
        "minimo": min(lista) if lista else None
    }
