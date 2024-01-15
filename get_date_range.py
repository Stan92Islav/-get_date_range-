'''Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:

start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно. Если start > end, функция должна вернуть пустой список.'''

from datetime import date

def get_date_range(start, end):
    a = list(range(start.toordinal(), end.toordinal()+1))
    if start < end:
        return [date.fromordinal(i) for i in a]
    elif start > end:
        return []
    elif start == end:
        return [start]

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')