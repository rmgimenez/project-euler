'''
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters 
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance 
with British usage.

resposta = 21124
'''
def qtd_letras_numero(numero):
	if numero in (1,2,6,10): return 3
	elif numero in (4,5,9): return 4
	elif numero in (3,7,8,40,50,60): return 5	
	elif numero in (11,12,20,30,80,90): return 6
	elif numero in (15,16,70): return 7
	elif numero in (13,14,18,19): return 8
	elif numero == 17: return 9
	else: 0

total = 0
for x in range(1,1001):
	milhar = 0
	centena = 0
	dezena = 0
	unidade = 0
	qtd_letras = 0

	numero = str(x)
	tam_numero = len(numero)
	if (tam_numero == 1):
		unidade = int(numero)
	elif tam_numero == 2:
		unidade = int(numero[1])
		dezena = int(numero[0])
	elif tam_numero == 3:
		unidade = int(numero[2])
		dezena = int(numero[1])
		centena = int(numero[0])
	elif tam_numero == 4:
		milhar = 1

	if dezena == 1:
		dezena = 0
		unidade = 10 + unidade

	if unidade != 0:
		qtd_letras = qtd_letras + qtd_letras_numero(unidade)
	if dezena != 0:
		qtd_letras = qtd_letras + qtd_letras_numero(dezena*10)
	if centena != 0:
		qtd_letras = qtd_letras + qtd_letras_numero(centena) + 7 # 100 - a/one hundred
		if unidade != 0 or dezena != 0:
			qtd_letras = qtd_letras + 3 # conta o and
	if milhar != 0:
		qtd_letras = qtd_letras + qtd_letras_numero(milhar) + 8 # 1,000 - a/one thousand

	total = total + qtd_letras
	print("x =",x)
	print("milhar =",milhar)
	print("centena =",centena)
	print("dezena =",dezena)
	print("unidade =",unidade)
	print("qtd letras =",qtd_letras)
	print("--------------------------")

	#qtd.append(qtd_letras_numero(x))

print("Total =", total)