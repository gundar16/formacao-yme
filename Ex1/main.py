# Recolher dados iniciais
nome = input("Qual é o teu nome? ")
idade = int(input("Quantos anos tens? "))
horas_sono = float(input("Quantas horas dormiste esta noite? "))
atividades = int(input("Quantas atividades tens planeadas para hoje? "))

# Energia inicial
energia = 50

# Ajustar energia com base nas horas de sono
if horas_sono < 5:
    energia -= 20
elif horas_sono < 7:
    energia -= 10
elif horas_sono >= 8:
    energia += 10

# Loop para ajustar energia conforme o número de atividades
for i in range(atividades):
    energia -= 5

# Loop para adicionar energia ao beber café
while True:
    cafe = input("Queres beber um café? (s/n): ").lower()
    if cafe == "s":
        energia += 5
        print("Energia aumentada! Energia atual:", energia)
    else:
        break

# Mostrar energia final com mensagem personalizada
print(f"{nome}, a tua energia final é {energia} pontos.")

if energia < 30:
    print("Estás mesmo a precisar de descansar!")
elif energia < 60:
    print("Estás a meio gás, mas ainda consegues dar conta do recado.")
else:
    print("Estás cheio de energia!")

