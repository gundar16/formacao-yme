import random

def criar_viagem():
    """
    Função para criar uma viagem com os dados fornecidos pelo user.

    Pede a autonomia atual do veículo, a capacidade total do veículo, o número de
    kilómetros que normalmente percorre num dia (tem de ser menor que a capacidade) e a
    distância total da viagem.

    Retorna um dicionário com as chaves "autonomia", "capacidade", "km_por_dia", "distancia",
    "dias_passados" e "passos_avaria".
    """

def reparar(viagem):
    """
    Função recursiva para reparar uma avaria. Enquanto a avaria não estiver reparada (passos_avaria != 0),
    pega o input do user e decrementa o número de etapas restantes. Se a avaria estiver reparada,
    imprime uma mensagem de sucesso e retorna a viagem.

    Retorna a viagem com as informações atualizadas.
    """

def abastecer(viagem):
    """
    Função para abastecer uma viagem. Incrementa a autonomia para o valor da capacidade
    e incrementa o número de dias passados.

    Retorna a viagem com as informações atualizadas.
    """

def conduzir(viagem):
    """
    Função para conduzir uma viagem com base na distância percorrida no dia anterior e uma condição
    aleatória. A condição pode ser "normal", "trânsito", "chuva", "subida", "descida", "pequena
    avaria" ou "grande avaria".

    O consumo de combustível é calculado com base na distância percorrida e na condição. Se
    a condição for "pequena avaria" ou "grande avaria", um número de passos de avaria é
    adicionado à viagem.

    Retorna a viagem com as informações atualizadas.
    """
    condicao = random.choice(["normal", "trânsito", "chuva", "subida", "descida", "pequena avaria", "grande avaria"])
    
def viajar(viagem):
    """
    Função para viajar com base em uma viagem. Imprime mensagens para o user e permite que ele escolha
    entre conduzir ou abastecer em cada dia. Se houver uma avaria, a função reparar é chamada
    e o número de passos de avaria é decrementado. O consumo de combustível é calculado
    com base na distância percorrida e na condição. Se a condição for "pequena avaria" ou
    "grande avaria", um número de passos de avaria é adicionado à viagem.

    Retorna a viagem com as informações atualizadas.
    """