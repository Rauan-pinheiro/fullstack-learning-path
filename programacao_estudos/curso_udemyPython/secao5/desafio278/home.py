# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
#é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

print('-='*30)
#data do empréstimo
data_inicio = datetime.strptime('20/12/2020', '%d/%m/%Y')
print('Data do empréstimo:', data_inicio.strftime('%d/%m/%Y'))
print('-='*30)

#data final do empréstimo (data de inicio mais 5 anos)
data_fim = relativedelta(years=5)
data_fim = data_fim + data_inicio
print('Data final do empréstimo',data_fim.strftime('%d/%m/%Y'))
print('-='*30)

#Mostre todas as datas de vencimento e o valor de cada parcela
total = 1_000_000
tempo_em_meses = 60
valor_parcela = total / tempo_em_meses

for mes in range(1,61):
    parcelas = data_inicio + relativedelta(months=mes)
    parcelas = parcelas.strftime('%d/%m/%Y')
    print(f'Parcela {mes:02} | Data:{parcelas} | Valor: R${valor_parcela:,.2f}')
