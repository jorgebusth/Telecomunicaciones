''' Sirve para calcular los pares de acuerdo a una nomenclatura
NP número de par, CC color de la cinta, CP color de par. '''

import math

def CPaNP(colorBase,colorSecundario):
	Blanco = 0
	Azul = 1
	Naranja = 2
	Verde = 3
	Cafe = 4
	Gris = 5
	Rojo = 5
	Negro = 10
	Amarillo = 15
	Violeta = 20

	if(colorBase == 'Blanco'):
		if(colorSecundario == 'Azul'):
			numPar = 1
		elif(colorSecundario == 'Naranja'):
			numPar = 2
		elif(colorSecundario == 'Verde'):
			numPar = 3
		elif(colorSecundario == 'Cafe'):
			numPar = 4
		elif(colorSecundario == 'Gris'):
			numPar = 5
		else:
			print('El color',colorSecundario,'no existe en el código de colores secundarios del cable multi par')


	elif(colorBase == 'Rojo'):
		if(colorSecundario == 'Azul'):
			numPar = 5
		elif(colorSecundario == 'Naranja'):
			numPar = 7
		elif(colorSecundario == 'Verde'):
			numPar = 8
		elif(colorSecundario == 'Cafe'):
			numPar = 9
		elif(colorSecundario == 'Gris'):
			numPar = 10
		else:
			print('El color',colorSecundario,'no existe en el código de colores secundarios del cable multi par')
			

	elif(colorBase == 'Negro'):
		if(colorSecundario == 'Azul'):
			numPar = 11
		elif(colorSecundario == 'Naranja'):
			numPar = 12
		elif(colorSecundario == 'Verde'):
			numPar = 13
		elif(colorSecundario == 'Cafe'):
			numPar = 14
		elif(colorSecundario == 'Gris'):
			numPar = 15
		else:
			print('El color',colorSecundario,'no existe en el código de colores secundarios del cable multi par')
			

	elif(colorBase == 'Amarillo'):
		if(colorSecundario == 'Azul'):
			numPar = 16
		elif(colorSecundario == 'Naranja'):
			numPar = 17
		elif(colorSecundario == 'Verde'):
			numPar = 18
		elif(colorSecundario == 'Cafe'):
			numPar = 19
		elif(colorSecundario == 'Gris'):
			numPar = 20
		else:
			print('El color',colorSecundario,'no existe en el código de colores secundarios del cable multi par')
			

	elif(colorBase == 'Violeta'):
		if(colorSecundario == 'Azul'):
			numPar = 21
		elif(colorSecundario == 'Naranja'):
			numPar = 22
		elif(colorSecundario == 'Verde'):
			numPar = 23
		elif(colorSecundario == 'Cafe'):
			numPar = 24
		elif(colorSecundario == 'Gris'):
			numPar = 25
		else:
			print('El color',colorSecundario,'no existe en el código de colores secundarios del cable multi par')
			

	else:
		print('El color',colorBase,'no existe en el código de colores base del cable multipar.')
		

	return numPar



def CP(numPar):
	if(numPar<26):
		colorPar = numPar
	elif(numPar > 25):
		secuencia = math.ceil(numPar / 25)*25
		colorPar = numPar - secuencia

	if(colorPar == 1):
		colorPar = 'Blanco Azul'
	elif(colorPar == 2):
		colorPar = 'Blanco Naranja'
	elif(colorPar == 3):
		colorPar = 'Blanco Verde'
	elif(colorPar == 4):
		colorPar = 'Blanco Cafe'
	elif(colorPar == 5):
		colorPar = 'Blanco Gris'
	elif(colorPar== 6):
		colorPar = 'Rojo Azul'
	elif(colorPar== 7):
		colorPar = 'Rojo Naranja'
	elif(colorPar== 8):
		colorPar = 'Rojo Verde'
	elif(colorPar== 9):
		colorPar = 'Rojo Café'
	elif(colorPar== 10):
		colorPar = 'Rojo Gris'
	elif(colorPar== 11):
		colorPar = 'Negro Azul'
	elif(colorPar== 12):
		colorPar = 'Negro Naranja'
	elif(colorPar== 13):
		colorPar = 'Negro Verde'
	elif(colorPar== 14):
		colorPar = 'Negro Café'
	elif(colorPar== 15):
		colorPar = 'Negro Gris'
	elif(colorPar== 16):
		colorPar = 'Amarillo Azul'
	elif(colorPar== 17):
		colorPar = 'Amarillo Naranja'
	elif(colorPar== 18):
		colorPar = 'Amarillo Verde'
	elif(colorPar== 19):
		colorPar = 'Amarillo Café'
	elif(colorPar== 20):
		colorPar = 'Amarillo Gris'
	elif(colorPar== 21):
		colorPar = 'Violeta Azul'
	elif(colorPar== 22):
		colorPar = 'Violeta Naranja'
	elif(colorPar== 23):
		colorPar = 'Violeta Verde'
	elif(colorPar== 24):
		colorPar = 'Violeta Café'
	elif(colorPar== 25):
		colorPar = 'Violeta Gris'

	return colorPar
	pass

def CC(numPar):
	colorCinta = math.ceil(numPar / 25)
	colorCinta = CP(colorCinta)
	return colorCinta


# Inicia programa principal

print('Este programa sirve para calcular los cables multipar de cobre de hasta 300 usuarios.\n\n')
ejecutar = 's'

while (ejecutar == 's'):

	print('\n\tMenú\n\n\t1. Número del par\n\t2. Color de la cinta\n\t3. Color del par\n\t4. Salir')
	opcion = input('\nDigite su opción (1-4): ')

	if(opcion == '1'):
		colorBase= input('Ingrese el color base del par: ')
		colorSecundario = input('Ingrese el color secundario del par: ')
		numPar = CPaNP(colorBase,colorSecundario)
		print(numPar)

	elif(opcion == '2'):
		numPar = float(input('\n\tIngresa el número de par: '))
		colorCinta = CC(numPar)
		print(colorCinta)

	elif(opcion == '3'):
		numPar = float(input('\n\tIngresa el número de par: '))
		colorPar = CP(numPar)
		print(colorPar)

	elif(opcion == '4'):
		print('\n\tGracias por utilizar este programa')
		break

	else:
		print('\n\t Error: Solo se acepta la opción del 1 al 4.\n')

	ejecutar = input('Desea realizar otro cálculo? s/n: ')
	if(ejecutar== 'n'):
		print('\n\tGracias por utilizar este programa')
