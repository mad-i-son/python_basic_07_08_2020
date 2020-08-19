"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
 заработной платы сотрудника. В расчете необходимо использовать формулу:
  (выработка в часах * ставка в час) + премия. Для выполнения расчета для
   конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

def wage_script(production_in_hours, rate_per_hour, premium):
    return (float(production_in_hours) * float(rate_per_hour)) + float(premium)

_, production_in_hours, rate_per_hour, premium = argv

print(f'Заработная плата сотрудника {wage_script(production_in_hours, rate_per_hour, premium)}')

