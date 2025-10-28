# importar o módulo funcoes
import funcoes

# Pedir ao utilizador a quantidade de números de Fibonacci
quantidade = int(input("Quantos números de Fibonacci queres gerar? "))

# Gerar a lista
lista_fib = funcoes.list_generator(quantidade)

# Calcular estatísticas
stats = funcoes.estatisticas(lista_fib)

# Exibir resultados
print("\n--- Sequência de Fibonacci ---")
print(lista_fib)

print("\n--- Estatísticas ---")
print(f"Tamanho: {stats['tamanho']}")
print(f"Somatório: {stats['somatorio']}")
print(f"Máximo: {stats['maximo']}")
print(f"Mínimo: {stats['minimo']}")
