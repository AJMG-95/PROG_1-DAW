from math import pi, sqrt
from math import trunc
import math

def problema_1():
    print("Encantado de conocerte")

def problema_2():
    numero = input("Escríbeme un número: ")
    print(numero)

def problema_3():
    numero_edad = int(input("Dime cual es tu edad: "))
    numero_edad += 1
    print(f"Tu edad el año que viene va a ser de {numero_edad}")

def problema_4():
    anio_actual = int(input("¿En qué año estamos?: "))
    fecha_nacimiento = int(input("Dime en qué año naciste: "))
    anios_usuario = anio_actual - fecha_nacimiento
    print(f"La edad que tienes es de {anios_usuario}")

def problema_5():
    nota_1 = float(input("Dime la primera nota que sacaste: "))
    nota_2 = float(input("Dime la segunda nota que sacaste: "))
    nota_final = (nota_1 + nota_2) / 2
    print(f"Tu nota final es de {nota_final}")

def problema_6():
    import math
    radio = float(input("Dime el radio del círculo: "))
    longitud = (2 * pi) * radio
    area = pi * radio ** 2
    print(f"la longitud del círculo es de {round(longitud)} y el area es de {round(area)}")

def problema_7():
    a = int(input("Introduce el primero número: "))
    b = int(input("Introduce el segundo número: "))
    if a == b:
        return True
    else:
        return False

def problema_8():
    numero = int(input("Dime cuantos años tienes: "))
    if numero >= 18:
        return True
    else:
        return False

def problema_9():
    numero = int(input("Escribeme un número: "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def problema_10():
    llueve = input("¿Hoy está lloviendo?: ")
    tareas = input("¿Completaste las tareas?: ")
    biblioteca = input("¿Necesitas ir a la biblioteca?: ")
    # yanderedev momento
    if llueve == "False" and tareas == "True" or biblioteca == "True":
        return True
    else:
        return False

def problema_11():
    manzana = int(input("kilo de mansanas ejje: "))
    pera = int(input("kilo de peras jej: "))

    precio_manzanas = manzana * 2.35
    precio_peras = pera * 1.95

    return "beneficio total es de " + str(precio_manzanas + precio_peras)

def problema_12():
    numero = int(input("Dime un número: "))
    return f"El valor absoluto es de {abs(numero)}"

def problema_13():
    notas_1 = float(input("Dime las notas del primer trimestre: "))
    notas_2 = float(input("Dime las notas del segundo trimestre: "))
    notas_3 = float(input("Dime las notas del tercer trimestre: "))
    calificaciones = (notas_1 + notas_2 + notas_3) / 3

    print(f"La calificacion final es de {round(calificaciones)} y la del expediente es de {calificaciones}")

def problema_14():
    import math
    numero = float(input("Dime un número: "))
    return round(numero)


def problema_15():
    base = float(input("Escribe el precio del producto: "))
    IVA = float(input("El IVA del producto: "))
    return f"El importe correspondiente es de {(base * IVA)}, y su iva es de {IVA}%"

def problema_16(numero):
    cont = 0
    while (numero + cont) % 7 != 0:
        cont += 1
    print(cont)

def problema_17(numero):
    multiplo = int(input("Qué numero quiere que sea el múltiplo: "))
    cont = 0
    while (numero + cont) % multiplo != 0:
        cont += 1
    print(cont)

def problema_18():
    base = int(input("Dime la base: "))
    altura = int(input("Dime la altura: "))
    area = (base * altura) / 2
    return area

def problema_19():
    import math
    a = int(input("Dime la letra a: "))
    b = int(input("Dime la letra b: "))
    c = int(input("Dime la letra c: "))
    dentro_ecuacion = b**2 -4 * a * c
    if dentro_ecuacion < 0:
        return "Es un número imaginario"
    x = ( - b + math.sqrt(dentro_ecuacion)) / 2 * a
    x_resta = (-b - math.sqrt(dentro_ecuacion)) / 2 * a
    return x, x_resta

def problema_20():
    segundos = int(input("Introduce una cantidad de segundos: "))

    return f"Son {(segundos)/3600} horas, {(segundos)/60} minutos y {segundos} en segundos"

def problema_21():
    milimetros = float(input("En milimetros: "))
    centimetros = float(input("En centimetros: "))
    metros = float(input("En metros: "))
    suma = (milimetros / 10) + centimetros + (metros * 100)
    print(f"Son {suma} en centimetros")


def problema_22():
    aranias = int(input("cuantas araña has cogio: "))
    hormigas = int(input("cuantas hormigas has cogio: "))
    cochinillas = int(input("cuantas cochinillas has cogio: "))
    suma = (aranias * 8) + (cochinillas * 14) + (hormigas * 6)
    return f"en total son {suma} patas"

def problema_23():
    infantil = int(input("¿Cuantas entradas infantiles quieres?"))
    adulto = int(input("¿Cuantas entradas de adultos quieres?"))
    suma = (adulto * 20) + (infantil * 15.50)
    if suma >= 100:
        return f" el precio es de {suma * 5 / 100} 5€ ya que el precio es más de 100 se le hará el descuento de un 5%"
    return f"El precio es de {suma} €"

def problema_24():
    import math
    numero_real = int(input("Dame un número real: "))
    print(sqrt(numero_real))

def problema_25():
    longitud_metros = float(input("¿Cuántos metros ha sido el lanzamiento?"))
    longitud_centimetros = round(longitud_metros) * 100
    return f"Ha conseguido {longitud_centimetros} centimetros en total"

def problema_26():
    numero = int(input("Escribe un número: "))
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

def problema_27():
    numero_1 = int(input("Escribe un número: "))
    numero_2 = int(input("Escribe un número: "))
    if numero_1 == numero_2:
        return "Son iguales"
    return "No son iguales"

def problema_28():
    numero_1 = int(input("Escribe un número: "))
    numero_2 = int(input("Escribe un número: "))
    if numero_1 > numero_2:
        return f"{numero_1} es mayor que {numero_2}"
    if numero_1 == numero_2:
        return f"Son iguales"
    return f"{numero_2} es mayor que {numero_1}"

def problema_29():
    numero_1 = int(input("Escribe un número: "))
    numero_2 = int(input("Escribe un número: "))
    if numero_1 > numero_2:
        return f"{numero_1} es mayor que {numero_2}"
    if numero_1 == numero_2:
        return f"Son iguales"
    return f"{numero_2} es mayor que {numero_1}"

def problema_30():
    numero = float(input("Escribe un número: "))
    if abs(numero) < 1 and numero != 0:
        return (f"El numero {numero} pertenece al grupo de casi-ceros")
    return (f"El numero {numero} no pertenece al grupo de casi-ceros")

def problema_31():
    lista = []
    for i in range (0, 2):
        numero = int(input("Escríbeme un número: "))
        lista.append(numero)
    return sorted(lista, reverse = True)

def problema_32():
    lista = []
    for i in range(0, 3):
        numero = int(input("número: "))
        lista.append(numero)
    lista_nueva = sorted(lista)
    print(lista_nueva[::-1])

def problema_33():
    import math
    a = int(input("Dime la letra a: "))
    b = int(input("Dime la letra b: "))
    c = int(input("Dime la letra c: "))
    dentro_ecuacion = b**2 -4 * a * c
    if dentro_ecuacion < 0:
        return "Es un número imaginario"
    x = ( - b + math.sqrt(dentro_ecuacion)) / 2 * a
    x_resta = (-b - math.sqrt(dentro_ecuacion)) / 2 * a
    return x, x_resta

def problema_34():
    numero = input("Dime un número: ")
    return len(numero)

def problema_35():
    nota = int(input("Dime que nota sacaste: "))
    if nota <= 4:
        print("Insuficiente")
    if nota == 5:
        print("Suficiente")
    if nota == 7 and 8:
        print("Notable")
    if nota == 9:
        print("Sobresaliente")
    if nota == 10:
        print("Matricula de honor")
    if nota == 6:
        print("Bien")

def problema_36():
    numero = int(input("Dime un número del 1 al 7: "))
    dias_semana = {1 : "lunes", 2 : "martes", 3 : "miercoles", 4 : "jueves", 5 : "viernes", 6 : "sabado", 7 : "domingo"}
    return dias_semana[numero]

def problema_37():
    numero = int(input("Dime un número del 1 al 7: "))
    dias_semana = {1 : "lunes", 2 : "martes", 3 : "miercoles", 4 : "jueves", 5 : "viernes", 6 : "sabado", 7 : "domingo"}
    return dias_semana[numero]

def problema_38():
    dia = int(input("Dime el día: "))
    mes = int(input("Dime el mes: "))
    anio = int(input("Dime el año: "))
    treinta = [4, 6, 9, 11]
    if dia > 28 and mes == 2:
        return "No es una fecha válida"
    if dia > 30 and mes in treinta:
        return "No es una fecha válida"
    return f"{dia}-{mes}-{anio}"

def problema_39():
    dia = int(input("Dime el día: "))
    mes = int(input("Dime el mes: "))
    anio = int(input("Dime el año: "))
    treinta = [4, 6, 9, 11]
    if dia > 28 and mes == 2:
        return "No es una fecha válida"
    if dia > 30 and mes in treinta:
        return "No es una fecha válida"
    if not anio % 4 and (anio % 100 or not anio % 400):
        print("Es bisiesto")
    return f"{dia}-{mes}-{anio}"

def problema_40():
    dia = int(input("Dime el día: "))
    mes = int(input("Dime el mes: "))
    anio = int(input("Dime el año: "))
    treinta = [4, 6, 9, 11]
    if dia > 28 and mes == 2:
        return "No es una fecha válida"
    if dia > 30 and mes in treinta:
        return "No es una fecha válida"
    if dia == 30 and mes in treinta:
        mes += 1
        dia = 1
    if dia == 31 and mes == 12:
        anio += 1
        dia = 1
        mes = 1
    if dia != 31 and mes != 12 and mes not in treinta:
        dia += 1
    return f"{dia}-{mes}-{anio}"

def problema_41():
    horas = int(input("Dime las horas: "))
    minutos = int(input("Dime los minutos: "))
    segundos = int(input("Dime los segundos: "))

    if segundos == 60:
        minutos += 1
        segundos = 0
    if minutos == 60:
        horas += 1
        minutos = 0

    if segundos != 60:
        segundos += 1

    return f"{horas}:{minutos}:{segundos}"

def problema_42():
    numero = int(input("Escribeme un número: "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

    if numero > 0:
        print("Es positivo")
    else:
        print("Es negativo")

    return numero ** 2

def problema_43():
    edad = 0
    i = 0
    suma = 0
    mayores = 0
    while edad != -1:
        edad = int(input("Edad: "))
        if edad >= 18:
            mayores += 1
        i += 1
        suma += edad
    resultado = suma / i
    return f"{round(resultado)} es la media de los alumnos y {mayores} son mayores de edad"



def problema_46():
    import random
    numero_1 = random.randint(0, 100)
    numero_2 = random.randint(0, 100)
    solucion = numero_1 + numero_2
    print(solucion)
    respuesta = int(input("Introduce un número: "))
    while respuesta != solucion:
        print("No es correcto")
        respuesta = int(input("Introduce un número: "))
    print("Acertaste")


def problema_47():
    numero = int(input("Introduce un número: "))
    for i in range(1, numero + 1):
        print(i)

def problema_48():
    numero = int(input("Introduce un número: "))
    for i in range(0, 100):
        solucion = numero * i
        print (f"{numero} x {i} = {numero * i}")
        if solucion > 100:
            break


def problema_49():
    cont = 0
    lista = []
    while cont != 10:
        numero = int(input("Introduce un número: "))
        lista.append(numero)
        cont += 1
    return sum(lista)/cont

def problema_50():
    numero = int(input("Introduce un número: "))
    if numero > 10:
        return "Tiene que ser del 1 al 10"
    for i in range(0, 11):
        print (f"{numero} x {i} = {numero * i}")

def problema_51():
    for i in range(0, 11):
        print(f"TABLA DEL {i}")
        for e in range(0, 11):
            print (f"{i} x {e} = {i * e}")

def problema_52():
    lista = []
    for i in range(0, 11):
        if i % 2 != 0:
            lista.append(i)
    print(lista)
    return sum(lista)

def problema_53():
    numero = int(input("Introduce un número: "))
    lista = []
    num_lista = 1
    for i in range(1, numero + 1):
        lista.append(i)
    for x in lista:
        num_lista = num_lista * x
    print(num_lista)

def problema_54():
    cont = 0
    lista = []
    suspensos = 0
    aprobados = 0
    while cont < 5:
        notas = int(input("Dime que nota sacaste: "))
        lista.append(notas)
        cont += 1
    for i in lista:
        if i < 5:
            suspensos += 1
        aprobados += 1
    return(f"Hay {suspensos} suspensos y {aprobados} aprobados")


def problema_55():
    cont = 0
    lista = []
    suspensos = 0
    aprobados = 0
    while cont < 6:
        notas = int(input("Dime que nota sacaste: "))
        lista.append(notas)
        cont += 1
    for i in lista:
        if i < 4:
            suspensos += 1
        aprobados += 1
    return(f"Hay {suspensos} suspensos y {aprobados} aprobados")

def problema_56():
    numero = int(input("Dime cuantas estrellitas kieres: "))
    for i in range(numero, 0, -1):
        print(i * "*")

def problema_57():
    numero = int(input("Dime un número decimal si kieres: "))
    binarios = []
    resto = 0
    while numero != 0:
        resto = numero % 2
        numero = numero // 2
        binarios.append(str(resto))
    alreve = binarios[::-1]
    print("".join(alreve))


def problema_58():
    cont = 0
    solucion = 0
    numero = input("Escribeme un número en binario: ")
    cont = len(numero)
    for i in str(numero):
        cont -= 1
        solucion +=  int(i) * (2 ** cont)
    return solucion

"""
def problema_59():
    horas = int(input("Dime las horas: "))
    minutos = int(input("Dime los minutos: "))
    segundos = int(input("Dime los segundos: "))
    segundos_pedidos = int(input("Introduceme los segundos que quieras pedir: "))
    if segundos_pedidos ==  60:

    if segundos == 60:
        minutos += 1
        segundos = 0
    if minutos == 60:
        horas += 1
        minutos = 0

    if segundos != 60:
        segundos += 1
"""

def problema_60():
    numero = int(input("Escribe un numero: "))
    def primos(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    for j in range(1, numero + 1):
        if primos(j):
            print(f"El numero {j} es primo")
        else:
            print(f"El número {j} no es primo ")


def problema_61(numero_filas):
    if numero_filas == 0:
        return [[1]]
    triangulo = problema_61(numero_filas - 1)
    ultima_fila = triangulo[-1]
    ultima_copia = ultima_fila
    ultima_fila = [0] + ultima_fila
    ultima_copia = ultima_copia + [0]
    nueva = list(map(lambda x, y: x + y, ultima_fila, ultima_copia))
    triangulo.append(nueva)
    return triangulo

def problema_62():
    n = int(input("Escribeme un número: "))
    estrellita = "* "
    espacio = " "
    for i in range(0, n + 1):
            print((i * estrellita + espacio).center(20))

def problema_63():
    numero_1 = int(input("Escribe el primer número: "))
    numero_2 = int(input("Escribe el segundo número: "))
    minimo = min(numero_1, numero_2)
    i = minimo
    while True:
        if numero_1 % i == 0 and numero_2 % i == 0:
            print(i)
            break
        i -= 1

def problema_64():
    numero_1 = int(input("Escribe el primer número: "))
    numero_2 = int(input("Escribe el segundo número: "))
    maximo = max(numero_1, numero_2)
    i = maximo
    while True:
        if i % numero_1 == 0 and i % numero_2 == 0:
            print(i)
            break
        i += 1

def problema_65():
    numero_1 = int(input("Escribe el primer número: "))
    numero_2 = int(input("Escribe el segundo número: "))
    numero_3 = int(input("Escribe el segundo número: "))
    minimo = min(numero_1, numero_2, numero_3)
    i = minimo
    while True:
        if numero_1 % i == 0 and numero_2 % i == 0 and numero_3 % i == 0:
            print(i)
            break
        i -= 1

def problema_66():
    numero = int(input("Escribe el primer número: "))
    cont = 1
    while True:
        if cont ** 2 < numero:
            cont += 1
        else:
            return f"el resultado es {cont - 1} y el resto es {abs(numero - ((cont - 1) ** 2))}"


def problema_67():
    print("Pulsa 1 si es dinero del banco")
    print("Pulsa 2 si es dinero de los bolsillos")
    print("Pulsa 3 si es dinero del cajon")
    print("Pulsa 4 si es dinero de la hucha")
    print("Pulsa 0 si quieres salir")
    saldo = 0
    numero = 1
    while numero != 0:
        numero = int(input("Introduce el número: "))
        if numero != 0:
            cantidad = int(input("Introduzca la cantidad: "))
            saldo += cantidad
            print("Pulsa 1 si es dinero del banco")
            print("Pulsa 2 si es dinero de los bolsillos")
            print("Pulsa 3 si es dinero del cajon")
            print("Pulsa 4 si es dinero de la hucha")
            print("Pulsa 0 si quieres salir")
        else:
            break
    return f"{saldo} €"

def problema_68():
    veces = int(input("Dime cuantas veces quieres que se repita: "))
    for i in range(0, veces):
        print("eco...")


def problema_69():
    num_1 = int((input("Dime el primer numero: ")))
    num_2 = int((input("Dime el primer numero: ")))
    for i in range(num_1 + 1, num_2):
        print(f"Los numeros comprendidos son... {i}")



def problema_70():
    list = []
    num_1 = int((input("Dime el primer numero: ")))
    num_2 = int((input("Dime el primer numero: ")))
    for i in range(num_1 + 1, num_2):
        list.append(i)
    return list

def problema_71():
    import math
    print("Si quieres calcular el area pulsa 1")
    print("Si quieres calcular el volumen pulsa 2")
    numero = (int(input("Pulsa 1 o 2: ")))
    if numero == 1:
        radio = int((input("Dime el radio: ")))
        altura = int((input("Dime el altura: ")))
        calculo_area = 2 * pi * radio * (altura + radio)
        print(f"El calculo del area es de {round(calculo_area)}")
    if numero == 2:
        radio = int((input("Dime el radio: ")))
        altura = int((input("Dime el altura: ")))
        volumen = pi * radio ** 2 * altura
        print(f"El calculo de el volumen es de {round(volumen)}")
    if numero != 1 and numero != 2:
        print("No es ninguna de las opciones")

def problema_72():
    num_1 = int((input("Dime el primer numero: ")))
    num_2 = int((input("Dime el primer numero: ")))
    return max(num_1, num_2)


def problema_73(letra):
    letra = letra.lower()
    vocales = ["a", "e", "i", "o", "u"]
    if letra in vocales:
        return True
    return False

def problema_74(numero):
    if numero >= 0:
        i = 1
        cont_divisores = 0
        while i <= numero and cont_divisores <= 2:
            if numero % i == 0:
                cont_divisores += 1
            i += 1
        if cont_divisores == 2:
            return True
        return False
    return False

def problema_75():
    num = int(input("Introduce un número: "))
    def problema_74(dato):
        if dato == 1 or dato == 2:
            return True
        if dato > 2:
            for n in range(2, dato):
                if dato % n == 0:
                    return False
                else:
                    return True
    cont = 0
    for j in range(1, num + 1):
        if num % j == 0 and problema_74(j):
            cont += 1
    print(cont)


def problema_76():
    print("---CALCULADORA-------")
    print("Dime que quieres hacer: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    opcion = int(input("Pon un número: "))
    if opcion == 1:
          num_1 = int((input("Dime el primer numero: ")))
          num_2 = int((input("Dime el segundo numero: ")))
          return sum(num_1, num_2)
    if opcion == 2:
          num_1 = int((input("Dime el primer numero: ")))
          num_2 = int((input("Dime el segundo numero: ")))
          return (num_1 - num_2)
    if opcion == 3:
          num_1 = int((input("Dime el primer numero: ")))
          num_2 = int((input("Dime el segundo numero: ")))
          return (num_1 * num_2)
    if opcion == 4:
          num_1 = int((input("Dime el primer numero: ")))
          num_2 = int((input("Dime el segundo numero: ")))
          return (num_1 / num_2)


def problema_77():
    import math
    radio = int(input("Indicame el radio que vas a usar: "))
    superficie = (4 * pi) * (radio ** 2)
    volumen = ((4 * pi) / 3) * (radio ** 3)
    return f"la superficie es de {round(superficie)} y su volumen es de {round(volumen)}"

def problema_79():
    n = int(input("Dime el rango de número que quieres: "))
    lista = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            lista.append(i)
    return lista

def problema_80():
    hora = int(input("Dime las horas: "))
    minutos = int(input("Dime los minutos: "))
    segundos = int(input("Dime los segundos: "))

    horas_a_segundos = hora * 3600
    minutos_a_segundos = minutos * 60
    segundos = horas_a_segundos + minutos_a_segundos + segundos

    return f"En total son {segundos} segundos"


def problema_81():
     num = int(input("Introduce un número: "))
     def problema_74(dato):
        if dato == 1 or dato == 2:
            return True
        if dato > 2:
            for n in range(2, dato):
                if dato % n == 0:
                    return False
                else:
                    return True
     lista = []
     for j in range(1, num + 1):
        if num % j == 0 and problema_74(j):
            lista.append(j)
     print(lista)

def problema_82():
    num_1 = int((input("Dime el primer numero: ")))
    num_2 = int((input("Dime el segundo numero: ")))
    suma = 0
    suma2 = 0
    for i in range(1, num_1):
        if num_1 % i == 0:
            suma += i
    for i in range(1, num_2):
        if num_2 % i == 0:
            suma2 += i
    if suma == num_2 and suma2 == num_1 and suma == num_2 and suma2 == num_1:
        print("Son numeros amigos <3")

def problema_83():
    import random
    cantidad = int(input("Cuantos numeros quieres en la lista?: "))
    minimo = int(input("Minimo de: "))
    maximo = int(input("Maximo de: "))
    lista = []
    cont = 0
    while cont != cantidad:
        numero = random.randint(minimo, maximo)
        lista.append(numero)
        cont += 1
    return lista

def problema_84():
    import random
    lista_enteros = []
    lista_reales = []
    lista_booleanos = []
    cont = 0
    while cont != 5:
        numero = random.uniform(0.0, 100.0)
        lista_enteros.append(numero)
        numero_2 = random.Random(0, 100)
        lista_reales.append(numero_2)
        numero_3 = random.choice([True, False])
        lista_booleanos.append(numero_3)
    print(lista_reales, lista_booleanos, lista_enteros)

def problema_85():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a = lista
    lista == a
    lista.append(0)
    print(a)
    print(lista)
    if lista == a:
        return True
    return False

def problema_86():
    import random
    lista = []
    cont = 0
    while cont != 10:
        numero = random.randint(1, 100)
        lista.append(numero)
        cont += 1
    return sum(lista)

def problema_87():
    n = int(input("cantidad de numeros que quieres: "))
    cont = 0
    num_positivos = 0
    num_negativos = 0
    ceros = 0
    while cont != n:
        numero = int(input("Introduzca un numero: "))
        if numero == 0:
            ceros += 1
        if numero > 0:
            num_positivos += numero
        if numero < 0:
            num_negativos += numero
        cont += 1
    return f"la media es {num_positivos / n} de numeros positivos, { num_negativos / n} de numeros negativos y {ceros} ceros totales"


def problema_88():
    cont = 0
    lista = []
    while cont != 5:
        numero = int(input("Introduce 5 numeros decimales: "))
        lista.append(numero)
        cont += 1
    for i in lista:
        print(i)

def problema_89():
    n = int(input("Introduce cuantos numeros desea introducir: "))
    lista = []
    cont = 0
    while cont != n:
        numero = int(input("Introduce un número: "))
        lista.append(numero)
        cont += 1
    lista = lista[::-1]
    for i in lista:
        print(i)


def problema_90(lista):
    return max(lista)

def problema_91():
    import random
    longitud = int(input("La longitud que quieras: "))
    fin = int(input("el numero del fin: "))
    lista = []
    while len(lista) != longitud:
        numero = randint(2, fin + 1)
        if numero % 2 == 0:
            lista.append(numero)
    print(lista)


def problema_92(lista):
    clave = int(input("Que clave quieres buscar en la lista?: "))
    cont = 0
    cont_lista = 0
    for i in lista:
        if i == clave:
            print(f"Está en la posición {cont}")
        else:
            cont += 1
            cont_lista += 1
    if clave not in lista:
        print("-1")


def problema_93(lista1, lista2):
    cont = 0
    resultado = 0
    if len(lista1) != len(lista2):
        print("No tienen la misma distancia entre ellas")
    for i in lista1:
            if i != lista2[cont]:
                cont += 1
            else:
                cont += 1
                resultado += 1
    return f"Tienes {resultado} coincidencias"


lista1 = [5, 8, 4, 23, 7, 1]
lista2 = [2, 8, 5, 23, 3, 1]

def problema_94(lista1):
    lista_nueva = []
    for i in lista1:
        if i not in lista_nueva:
            lista_nueva.append(i)
    while len(lista_nueva) != len(lista1):
        numero = randint(0, 50)
        if numero not in lista_nueva:
            lista_nueva.append(numero)
    print(lista_nueva)

def problema_95(lista1):
    lista_pares = []
    lista_impares = []
    for i in lista1:
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    print(lista_impares, lista_pares)

def problema_96():
    lista_nueva = []
    valor = int(input("Introduce un valor: "))
    for i in lista1:
        if i < valor:
            lista_nueva.append(i)
    print(lista_nueva)

def problema_97():
    print(lista1)
    posicion = int(input("¿Que posición del numero es del que quieres borrar?"))
    cont = 0
    lista_nueva = []
    for i in lista1:
        cont += 1
        if posicion != cont:
            lista_nueva.append(i)
    print(lista_nueva)

def problema_98():
    import random
    cont = 0
    lista_numeros = []
    while cont != 5:
        numeros = int(input("Dime tus numeros favoritos: "))
        lista_numeros.append(numeros)
        cont += 1
    while len(lista_numeros) > 1:
        for i in lista_numeros:
            suerte = random.choice(lista_numeros)
            if i == suerte:
                lista_numeros.remove(suerte)
            suerte2 = random.choice(lista_numeros)
            if i == suerte2:
                lista_numeros.remove(suerte2)
        media = (suerte + suerte2) / 2
        lista_numeros.append(round(media))
    print(lista_numeros)



def problema_99():
    import random
    dificultad = int(input("Dime cuantos dígitos quieres: "))
    cont = 0
    lista_numeros = []
    lista_tuya = []
    while cont != dificultad:
        numero = random.randint(0,9)
        lista_numeros.append(numero)
        cont += 1
    cont = 0
    print(lista_numeros)
    while cont != dificultad:
        llave = int(input("Dime los numeros de la caja secreta: "))
        lista_tuya.append(llave)
        cont += 1
    if lista_numeros == lista_tuya:
        return "Acertaste!!"
    return "Fallaste :("

def problema_100():
    lista = [[], [], [], [], []]
    n = 0
    for i in lista:
        m = 0
        for j in range(0, 5):
            formula = 10 * n + m
            i.append(formula)
            m += 1
            n += 1
    print(lista)


def problema_101():
    lista = [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14], [20, 21, 4, 23, 24], [30, 31, 32, 33, 34], [40, 41, 42, 43, 44]]
    clave = int(input("Dime que clave quieres buscar: "))
    lista_nueva = []
    for i in range (0, len(lista)):
        for f in range(0, len(lista[i])):
            if clave == lista[i][f]:
                lista_nueva.append([i, f])
    print(lista_nueva)

def problema_102():
    todos = []
    cont = 0
    sueldo = 0
    suma = 0
    while sueldo != -1:
        sueldo = int(input("Dime los sueldos que quieras poner: "))
        if sueldo == -1:
            break
        else:
            todos.append(sueldo)
        cont += 1
    for i in todos:
        suma += i
        suma = suma / cont
    return f"{sorted(todos)}, {max(todos)}, {round(suma)}"

def problema_103():
    lista = [[3, 5, 6], [4, 5, 6], [6, 6, 6], [3, 2, 1], [0, 0, 0]]
    posicion = int(input("Que nota de que niño quieres saber: "))
    suma = 0
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            if posicion == i:
                suma += j
    return f"{round(suma/3)} Es la nota final "


def problema_104():
    lista = [["lugar_0"], ["lugar_1"], ["lugar_2"], ["lugar_3"], ["lugar_4"]]
    posicion = (int(input("En qué posición estás?: ")))
    llegar = (int(input("A que posición quieres llegar?: ")))
    cont = 0
    for i in range(0, len(lista)):
        for j in range(0, len(lista[i])):
            if posicion + 1 == llegar or posicion - 1 == llegar:
                return "Puedes pasar directamente al sitio"
            return "Tienes que atravesar lugares intermedios"

def problema_105():
    lista = [10, 1, 5, 8, 9, 2]
    numero = int(input("De cuanto en cuanto lo quieres: "))
    lista_nueva = []
    suma = 0
    for i in range(0, (len(lista) - (numero - 1))):
        suma = 0
        for j in range(numero):
            suma += lista[i + j]
        lista_nueva.append(suma)
        print(lista_nueva)

def problema_106_107():
    resultado = []
    cuadrado =  [
	[ 4, 15, 14,  1],
	[ 9,  6,  7, 12],
	[ 5, 10, 11,  8],
	[16,  3,  2, 13]
]
    #SUMA DE FILAS
    for i in range(0, len(cuadrado)):
        suma = 0
        for j in range(0, len(cuadrado[i])):
            suma += cuadrado[i][j]
    resultado.append(suma)
    #SUMA COLUMNAS
    for j in range(0, len(cuadrado[i])):
        suma = 0
        for i in range(0, len(cuadrado)):
            suma += cuadrado[i][j]
    resultado.append(suma)
    suma = 0
    #SUMA DIAGONAL ARRIBA ABAJO
    for n in range(0, len(cuadrado)):
        suma += cuadrado[n][n]
    resultado.append(suma)
    suma = 0
    #SUMA DIAGONAL ABAJO ARRIBA
    for m in range(0, len(cuadrado)):
        m = m - 1
        suma += cuadrado[m][m]
    resultado.append(suma)
    cont = 0
    print(resultado)
    cont += 1
    for h in resultado:
        if h != resultado[cont]:
            return "No es un numero magico"
    return "Es un numero magico"


def problema_108():
    frase1 = str(input("Dime una frase: "))
    frase2 = str(input("Dime una frase: "))
    if len(frase1) > len(frase2):
        print("La primera frase tiene más carácteres")
    else:
        print("La segunda frase tiene más carácteres")

def problema_109():
    contrasenia = str(input("Introduce la contraseña: "))
    clave = ""
    while clave != contrasenia:
        clave = str(input("Dime una palabra: "))
        if clave > contrasenia:
            print("Es menor alfabeticamente")
        else:
            print("Es mayor alfabeticamente")
        if clave == contrasenia:
            return "Acertaste!"

def problema_110():
    contrasenia = str(input("Introduce la contraseña: "))
    clave = ""
    print(len(contrasenia) * "*")
    intento = (input("Introduzca una palabra: "))
    while contrasenia != intento:
        for i in range(len(contrasenia)):
            if contrasenia[i] == intento[i]:
                clave += intento[i] + " "
            else:
                clave += "* "
        print(clave)
        clave = ""
        intento = (input("Introduzca una palabra: "))
    print("Acertaste!")

def problema_111():
    cadena = input("Indicame la cadena: ")
    cont = 0
    for i in cadena:
        if i == " ":
            cont += 1
    print(cont)
    print(len(cadena))

def problema_112():
    cadena = input("Indicame la cadena: ")
    return(cadena[::-1])

def problema_113():
    cadena = input("Indicame la cadena: ")
    vocales = ["á", "é", "í", "ó", "ú", "a", "e", "i", "o,", "u", "Á", "É", "Í", "Ó", "Ú", "A", "E", "I", "O", "U"]
    cadena_final = ""
    for i in cadena:
        if i not in vocales:
            cadena_final += i
    print(cadena_final)

def problema_115():
    palabra = ""
    palabra = palabra.lower()
    final_palabra = ""
    while palabra != "fin":
        palabra = input("Introduce una palabra: ")
        if palabra == "fin":
            break
        final_palabra += palabra + " "
    print(final_palabra)


def problema_116():
    frase = input("Introduce una frase: ")
    frase = frase.lower().replace(" ", "")
    frase_alreve = frase[::-1].lower()
    print(frase_alreve)
    print(frase)
    if frase_alreve == frase:
        return "Si es un lainnodruque de esos"
    return "No es"

def problema_117():
    secuencia1 = ["e", "i", "k", "m", "p", "q", "r", "s", "t", "u", "v"]
    secuencia2 = ["p", "v", "i", "u", "m", "t", "e", "r", "k", "q", "s"]
    palabra = input("Introduce una palabra: ")
    palabra_nueva = ""
    for i in palabra:
        if i in secuencia1:
            for n in range (len(secuencia1)):
                if i == secuencia1[n]:
                    palabra_nueva += secuencia2[n]
        else:
            palabra_nueva += i

def problema_118():
    palabra1 = input("Dime la primera palabra: ")
    palabra2 = input("Dime la segunda palabra: ")
    lista1 = []
    lista2 = []
    for i in palabra1:
        lista1.append(i)
    for n in palabra2:
        lista2.append(n)

    for m in lista1:
        if m in lista2:
            lista2.remove(m)
    if lista2 == []:
        return "Es un anagrama"
    return "No es un anagrama"



def problema_123():
    while True:
        try:
            numero = int(input("Escribeme un número: "))
        except ValueError:
            print("Eso no es un número valido!")
        else:
            return f"Correcto {numero}"


#! DOCUMENTOS DE TEXTO

def problema_124():
    nombre = input("Escribe el archivo que quieres abrir y leer: ")
    f = open(f'{nombre}', 'r')
    print(f.read())

def problema_125():
    numeros = input("Indica el archivo: ")
    lista = []
    f = open(numeros, 'r')
    for i in f.readline():
        if i != " " and i != "\n":
            lista.append(int(i))

    return f"La suma es {sum(lista)} y la media es {round(sum(lista) / len(lista))}"



def problema_126():
    while True:
        try:
            edad = int(input("Dime tu edad: "))
            estatura = float(input("Dime tu estatura: "))
        except ValueError:
            print("No es correcto lo que me has dicho!")
        else:
            print("Correcto")

def problema_127():
    numeros = input("Indica el archivo: ")
    lista = []
    f = open(numeros, 'r')
    for i in f.readlines():
        if i != " " and i != "\n":
            lista.append(int(i))
    return(sum(lista))

def problema_128():
    archivo = input("¿En qué archivo quieres que se guarde?: ")
    f = open(archivo, 'a+')
    escribir = ""
    lista = []
    cont = 0
    f.read()
    while escribir != "fin":
            escribir = input("Dime lo que quieres escribir: ")
            lista.append(f"{escribir}\n")
            if escribir != "fin":
                f.writelines(lista[cont])
                cont += 1
            else:
                f.close()

def problema_129():
    archivo = input("¿Qué archivo quieres copiar?: ")
    f = open(archivo, 'r')
    nuevo = open(f"copia_de_{archivo}", 'a+')
    lista = []
    cont = 0
    for i in f.readlines():
        lista.append(i)
        nuevo.writelines(lista[cont])
        cont += 1

def problema_130():
    archivo = input("¿Que archivo quieres ver?: ")
    if archivo != "":
        f = open(f"{archivo}", 'r')
        for i in f.readlines():
            print(i)
    else:
        print("Este es el de prueba: ")
        w = open("prueba.txt", 'r')
        for q in w.readlines():
            print(q)


def problema_131():
    import sys
    archivo = sys.argv[1]
    if archivo != "":
        f = open(f"{archivo}", 'r')
        for i in f.readlines():
            print(i)
    else:
        print("Este es el de prueba: ")
        w = open("prueba.txt", 'r')
        for q in w.readlines():
            print(q)


def problema_132():
    nombre = input("Dime tu nombre: ")
    edad = input("Dime la edad que tienes: ")
    f = open("datos.txt", 'a+')
    lista = []
    lista.append(nombre)
    lista.append(edad)
    for i in lista:
        f.writelines(f"{i}\n")
    f.close()

def problema_133():
    archivo1 = input("Dime el archivo 1: ")
    archivo2 = input("Dime el archivo 2: ")
    lista = []
    f = open(archivo1, "r")
    w = open(archivo2, "r")
    for i in f.readlines():
            lista.append(i)
    for q in w.readlines():
            lista.append(q)
    print(lista)
    lista = sorted(lista)
    a = open("archivo3.txt", 'a+')
    for l in lista:
        a.writelines(l)
    f.close()
    a.close()
    w.close()

def problema_134():
    f = open('carta.txt', 'r')
    cont_lineas = 0
    cont_caracteres = 0
    espacios_blancos = 0
    lista = []
    for i in f.readlines():
        cont_lineas += 1
    print(cont_lineas)
    f = open("carta.txt", 'r')
    for w in f.readlines():
        if w != " ":
            cont_caracteres += len(w)
    print(cont_caracteres)
    f = open("carta.txt", 'r')
    for q in f.readlines():
        lista += q.split()
    print(len(lista))

def problema_135():
    f = open("numeros.txt", 'r')
    lista = []
    for i in f.readlines():
        caracter = "".join(i.split("\n"))
        if caracter != '':
            lista.append(caracter)
    print(f"{min(lista)} {max(lista)}")


def problema_136():
    f = open("firmas.txt", 'r')
    nombre = input("Inserte una firma: ")
    lista = []
    for i in f.readlines():
        amigos = "".join(i.split("\n"))
        lista.append(amigos)
    f.close()
    w = open("firmas.txt", 'w')
    if nombre not in lista:
        lista.append(nombre)
        for q in lista:
            w.writelines(f"{q}\n")
    f.close()
    print(lista)

def problema_137():
    archivo = input("Inserte el archivo que quieras ver: ")
    f = open(archivo, 'r')
    dato = "mas"
    texto = ""
    while dato == "mas":
        for i in f.readlines(24):
            texto += i
        print(texto)
        dato = input("Quieres ver más?: ")

def problema_138():
    lista = []
    cadena = input("Dime una cadena de numeros: ")
    for i in cadena:
        if i.isdigit():
            lista.append(int(i))
    print(lista)

#! EJERCICIOS XML:

def problema_139():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()

    for socio in raiz.iter("socio"):
        nombre = socio.find("nombre").text
        id_socio = socio.get("id")
        print([int(id_socio)], nombre)

def problema_140():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    cont = 0
    for socio in raiz.iter("socio"):
        cont += 1
    print(cont)

def problema_141():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    cadena = "Avda. de Huelva, s/n"

    for direccion in raiz.iter("direccion"):
        direccion.text = cadena
    arbol.write('club.xml')


def problema_142():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    calle = "Calle Ancha, 35"
    direccion = arbol.find("socios/socio[@id = '1']/direccion")
    direccion.text = calle
    arbol.write("club.xml")

def problema_143():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()

    for elemento in raiz.findall("socios/socio"):
        socio_id = elemento.get("id")
        if socio_id == "51":
            raiz.find("socios").remove(elemento)
        arbol.write("club.xml")

def problema_144():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    telefono = ET.Element('telefono')
    telefono.text = "666555444"
    for elemento in raiz.findall("socios/socio"):
        socio_id = elemento.get("id")
        if socio_id == "1":
            elemento.append(telefono)
    arbol.write("club.xml")

def problema_145():
    import xml.etree.ElementTree as ET
    arbol = ET.parse('club.xml')
    raiz = arbol.getroot()
    diccionario = {}
    for socio in raiz.iter("socio"):
        nombre = socio.find("nombre").text
        fecha_alta = socio.find("alta").text
        diccionario[nombre] = fecha_alta
    resultado = sorted(diccionario.items(), key = lambda x: x[1])
    for nombre, _ in resultado:
        print(nombre)
