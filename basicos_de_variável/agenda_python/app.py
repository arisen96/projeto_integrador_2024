# Começamos importando as bibliotecas que utilizaremos.
import pandas as pandas
from datetime import datetime, timedelta


# criamos aqui, um dataframe com horarios num período de 0 a 9
horarios = pandas.date_range(start=datetime.now().replace(second=0, microsecond=0, minute=0), periods=10, freq='H')
agenda = pandas.DataFrame({'Horário': horarios, 'Cliente': [None]*len(horarios)})



# Função para fazer um agendamento do cliente
def agendar_cliente(horario, cliente):
    global agenda
    if horario in agenda['Horário'].values:
        agenda.loc[agenda['Horário'] == horario, 'Cliente'] = cliente
    else:
        print("Horário inválido")



# revela os horários que estão disponíveis.
print("Horários disponíveis:")
print(agenda)


# aqui será exibido no terminal os horários disponíveis para agendamento.
print("Escolha um dos horários disponíveis para agendamentos: ")
for idx, row in agenda.iterrows():
    print(f"{idx}: {row['Horário']}")


# essa parte final do código faz com que o usuário coloque dados para o agendamento.
horario_idx = int(input("Digite o índice do horário do agendamento: "))
horario_input = agenda.loc[horario_idx, 'Horário']
cliente_input = input("Digite o nome do cliente: ")
agendar_cliente(horario_input, cliente_input)
print(agenda)
