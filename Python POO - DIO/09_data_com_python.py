from datetime import date, datetime, time, timedelta

d = date(2022,10,11)
print(d)
print(date.today())


data_hora = datetime(2023,7,10,10,30,20)
print(data_hora)

hora = time(10,20,0)
print(hora)

#---------------------------- Manipulando datas com timedelta()----------------------------------
#Criando data e hora 
d1 = datetime(2023,7,19)
print(d1) # 2023-07-19 13:45:00

#Adicionando uma semana
d1 = d1 + timedelta(weeks=1)
print(d1) #2023-07-29 13:45:00