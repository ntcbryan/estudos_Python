from datetime import datetime, timedelta

#Neste exemplo uma pessoa tem um funcionario e ele vai estimar a 
#demora para lavar o carro dependendo do tamanho do veiculo

tipo_carro = "P" # P, M OU G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficara ate {data_estimada}')
if tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficara ate {data_estimada}')
if tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficara ate {data_estimada}')
    