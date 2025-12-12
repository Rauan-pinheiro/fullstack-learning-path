#pegando data e hora --> date.now() e timezones
#link para ver as timezones --> https://en.wikipedia.org/wiki/list_of_tz_database_time_zones

from datetime import datetime
from pytz import timezone

#data do meu computador
data_meu_computador = datetime.now()
print(data_meu_computador)

print('-'*10)

#data da região de Tokyo
data_tokyo = datetime.now(timezone('Asia/Tokyo'))
print(data_tokyo)
