import math 
import datetime
print(math.sqrt(81))
print(round(math.pi))
print(math.pi)
print(round(34.267, 2))
print(math.ceil(3.56))
print(math.floor(4.56))


today = datetime.date.today()
print(today)
tommorow = today + datetime.timedelta(days=1)
print(tommorow)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)