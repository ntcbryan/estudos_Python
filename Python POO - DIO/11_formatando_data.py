 
import datetime

d = datetime.datetime.now()
print(d)

print(d.strftime("%d/%m/%y"))  # 10/04/24

print(d.strftime("%d/%m/%y %H %M")) # 10/04/24 19 55

print(d.strftime("%d %m %y")) # 10 04 24

#Convertendo string para datetime
date_string = "20/07/2023 15:30"
# aqui precisamos passar todas as infos que passamos na string, ex se na string tem D / M / Y / H / M e eu passar só D / M / Y, vai dar erro
d2 = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")  

print(d2) #2023-07-20 15:30:00
print(type(d2)) # <class 'datetime.datetime'>