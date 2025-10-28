# Importar as funções necessárias do módulo funcoes
from funcoes import criar_viagem, viajar

# Criar uma viagem com os dados fornecidos pelo user
viagem = criar_viagem();

# Iniciar a viagem
viajar(viagem)

# Verificar se a viagem foi concluída com sucesso
if viagem["distancia"] == 0:
    print("\nViagem concluída!\n")
    print(f"Autonomia final: {viagem['autonomia']}")
    print(f"Dias passados: {viagem['dias_passados']}")
else:
    print("\nAcabou a energia antes de chegares ao destino! Planeia melhor para a próxima")