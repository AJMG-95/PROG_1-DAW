# Datos personales
nombre = 'Antonio jesús Marchena'
print(nombre)
edad = 26
altura = 1.70
peso = 67.8

# Clasificación según la altura: Baloncesto > 1.80, Tenies <= 1.80
deporte = 'Baloncesto' if altura > 1.80 else 'Tenis' if altura <= 1.80 and altura > 1.50 else 'Golf'
print(deporte)
