'''
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from time import time
start = time()

import funcoes

dia_semana = 1 # 1 = segunda-feira / 7 = domingo
total_domingo_inico_mes = 0

def proximo_dia_semana(dia_atual):
	if dia_atual == 7:
		return 1
	else:
		return dia_atual + 1

for y in range(1900, 2001):
	for m in range(1,13):
		if m in (4,6,9,11): # meses com 30 dias
			for d in range(1,31):
				if (d == 1 and y != 1900 and dia_semana == 7):
					total_domingo_inico_mes += 1
				dia_semana = proximo_dia_semana(dia_semana)

		elif m in (1,3,5,7,8,10,12): # meses com 31 dias
			for d in range(1,32):
				if (d == 1 and y != 1900 and dia_semana == 7):
					total_domingo_inico_mes += 1
				dia_semana = proximo_dia_semana(dia_semana)
		else: # fevereiro
			if funcoes.is_leap_year(y):
				for d in range(1,30): # se o ano for bissexto fevereiro terá 29 dias
					if (d == 1 and y != 1900 and dia_semana == 7):
						total_domingo_inico_mes += 1
					dia_semana = proximo_dia_semana(dia_semana)
			else:
				for d in range(1,29): # se o ano não for bissexto fevereiro terá 28 dias
					if (d == 1 and y != 1900 and dia_semana == 7):
						total_domingo_inico_mes += 1
					dia_semana = proximo_dia_semana(dia_semana)

print(total_domingo_inico_mes)

print("Time: {0} secs".format(time()-start))

# resolvido