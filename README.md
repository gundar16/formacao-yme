# Formação YME

## Ex1

### Calculadora de Energia Diária

Objetivo: criar um programa que ajuda o utilizador a estimar a sua energia durante o dia com base nas suas horas de sono e na quantidade de atividades que faz.

Segue os seguintes passos:
- Cria e recolhe os dados para as variáveis iniciais através do comando input (nome, idade, horas de sono e número de atividades planeadas);
- Cria a variável “energia” fornecendo-lhe um valor inicial (por ex 50);
- Usa condições para alterar o valor da energia de acordo com as horas de sono;
- Usa um loop para ajustar a energia conforme o número de atividades realizadas;
- Usa outro loop para aumentar a energia enquanto o utilizador quiser beber café (dica: usa o comando input para recolher esse desejo);
- Exibe a energia final e uma pequena mensagem que depende dessa quantidade.

## Ex2

### O Consultor de Sequências

Objetivo: criar um programa dividido em dois ficheiros que permite a realização de operações com sequências numéricas, incluindo o cálculo de números de Fibonacci.

Segue os seguintes passos:
- Cria dois ficheiros: “main.py” e “funcoes.py”;
- No ficheiro relativo às funções, cria:
  - uma função recursiva “fibonacci(n)”;
  - uma função “list_generator(x)” que gere uma lista com os x primeiros números de fibonacci;
  - uma função que devolva um dicionário com as estatísticas da lista (tamanho, somatório, valores máximo e mínimo);
- No ficheiro principal, importa o módulo, pede a quantidade através do comando input, chama as funções criadas e exibe todos os resultados (lista e estatísticas).

## Ex3

### Gestor de Viagem de Carro

Contexto: O utilizador vai fazer uma viagem longa de carro e quer gerir a sua autonomia durante o percurso. Até ao destino surgem decisões que afetam o consumo e o tempo de viagem. A ideia é nunca ficar sem energia e chegar ao destino no menor tempo.

Objetivo: Criar um programa que:
- recolhe informações sobre o carro e o percurso;
- simula o avanço da viagem dia a dia, calculando o seu estado;
- permite o utilizador tomar decisões (parar, conduzir, recarregar, etc.);
- reage a eventos aleatórios (ex: trânsito, bom tempo, avarias);
- exibe o estado final da viagem.

Num ficheiro secundário é necessário criar todas as funções auxiliares:
- “criar_viagem()” que pede os valores iniciais (“autonomia”, “capacidade”, “km_por_dia” e “distancia”) e devolve um dicionário com o estado inicial da viagem (valores anteriores + “dias_passados” e “passos_avaria”, ambos a 0);
- “abastecer(viagem)” que aumenta 1 dia e a energia até ao máximo;
- “reparar(viagem)” que, recursivamente (e com um input), repara a avaria existente;
- “conduzir(viagem)” que aumenta 1 dia e faz as alterações necessárias (exibindo os resultados) com base nos km_por_dia e num dos eventos (escolhido aleatoriamente) normal, trânsito, chuva, subida, descida, pequena avaria ou grande avaria;
- “viajar(viagem)” que contém o loop que simula a viagem, onde é reparada a avaria existente ou é pedida uma ação que é concretizada.

No ficheiro principal:
- Importar funções necessárias do ficheiro anterior;
- Criar uma variável “viagem” e atribuir-lhe o valor retornado pela função “criar_viagem”;
- Chamar a função “viajar” com a viagem criada;
- Exibir uma mensagem final dependendo do motivo de término da viagem.
