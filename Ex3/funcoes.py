import random

# Função para criar uma viagem com os dados fornecidos pelo user
def criar_viagem():

    print("\nA recolher dados para criar a viagem...\n")

    autonomia = input("Introduz a autonomia atual do veículo em km: ")
    capacidade = input("Introduz a capacidade total do veículo em km: ")
    km_por_dia = input("Introduz o número de kilómetros que normalmente percorres num dia (tem de ser menor que a capacidade): ")
    distancia = input("Introduz a distância total da viagem: ")
    
    return {
        "autonomia": float(autonomia),
        "capacidade": float(capacidade),
        "km_por_dia": float(km_por_dia),
        "distancia": float(distancia),
        "dias_passados": 0,
        "passos_avaria": 0
    }

# Função recursiva para reparar avarias
def reparar(viagem):
    if viagem["passos_avaria"] == 0:
        print("\nAvaria reparada com sucesso!\n")
        return viagem
    input(f"Pressiona uma tecla para continuar a reparação ({viagem['passos_avaria']} etapas restantes)... ")
    viagem["passos_avaria"] -= 1
    return reparar(viagem)

# Função para conduzir uma viagem num dia e atualizar os dados da viagem
def conduzir(viagem):
    print("\nA conduzir...")

    km_por_dia = viagem["km_por_dia"]

    condicao = random.choice(["normal", "trânsito", "chuva", "subida", "descida", "pequena avaria", "grande avaria"])
    if condicao == "trânsito":
        km_percorridos = km_por_dia * 0.75
        consumo = km_percorridos * 1.35
    elif condicao == "chuva":
        km_percorridos = km_por_dia * 0.85
        consumo = km_percorridos
    elif condicao == "subida":
        km_percorridos = km_por_dia
        consumo = km_percorridos * 1.4
    elif condicao == "descida":
        km_percorridos = km_por_dia
        consumo = km_percorridos * 0.6
    elif condicao == "pequena avaria" or condicao == "grande avaria":
        km_percorridos = km_por_dia * 0.5
        consumo = km_percorridos
    else:
        km_percorridos = consumo = km_por_dia

    viagem["autonomia"] -= consumo
    viagem["distancia"] -= km_percorridos
    viagem["dias_passados"] += 1

    if condicao == "pequena avaria": viagem["passos_avaria"] = 3
    elif condicao == "grande avaria": viagem["passos_avaria"] = 8

    if viagem["autonomia"] < 0:
        consumo += viagem["autonomia"]
        viagem["autonomia"] = 0

    if viagem["distancia"] < 0:
        km_percorridos += viagem["distancia"]
        viagem["distancia"] = 0

    if condicao != "normal": print(f"\nCondição: {condicao}")
    else: print("\nCondição: nenhuma!")
    print(f"\nPercorreste {km_percorridos} km e consumiste {consumo} km\n")

    return viagem

# Função para abastecer o veículo e atualizar os dados da viagem
def abastecer(viagem):
    viagem["autonomia"] = viagem["capacidade"]
    viagem["dias_passados"] += 1
    return viagem

# Função principal para gerir a viagem
def viajar(viagem):

    print("\nA iniciar a viagem...\n")

    while viagem["distancia"] != 0 and viagem["autonomia"] != 0:
        print(f"--- Dia {viagem['dias_passados'] + 1} ---\n")
        print(f"Distância restante: {viagem['distancia']} km\n")
        print(f"Autonomia: {viagem['autonomia']} km\n")
        if viagem["passos_avaria"] != 0:
            print("\nOh não! Tens uma avaria para resolver\n")
            input(f"Pressiona uma tecla para iniciar a reparação ({viagem['passos_avaria']:.2f} passos restantes)")
            viagem["passos_avaria"] -= 1
            reparar(viagem)
            viagem["dias_passados"] += 1
        else:
            print("\nEscolhe uma ação:\n")
            print("1 - Conduzir\n")
            print("2 - Abastecer\n")
            n = input("> ")

            if int(n) == 1:
                conduzir(viagem)
            else:
                abastecer(viagem)

    return viagem