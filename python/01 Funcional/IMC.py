# Cláculo del IMC de una persona
# Pre: peso > 0 and altura != 0
#  imc(peso: float, altura: float) --> float
# Post: imc(a, b) es el indice de masa corporal de una persona con peso a y altura b
#   peso a (en kg) y altura b (en m)
imc = lambda a, b: a / b ** 2
print (imc)
