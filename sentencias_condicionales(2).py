#Sentencias condicionales
# el switch en python no existe
#la linea de abajo no es un comentario como tal
# sino una especificacion de caracterizacion
#encoding: utf-8
edad=17
m_edad=18
if edad>=m_edad:
	print ("Eres mayor de edad")
else:
	print ("No eres mayor de edad")
print ("Hola esto se ejecutara siempre")

if edad>=0 and edad<18:
	print ("Eres un niño")
elif edad>=18 and edad<27:
	print ("Eres un joven")
elif edad>=27 and edad<60:
	print ("Eres un adulto")
else:
	print ("Eres de la tercera edad.")
