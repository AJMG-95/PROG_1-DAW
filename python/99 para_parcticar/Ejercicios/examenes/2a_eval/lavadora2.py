''' Lavadora (4Pts)

    Programar en Python un modelo orientado a objetos del funcionamiento de una
      lavadora.

    Una lavadora:

    Puede estar encendida o apagada (por defecto está apagada).

    En cada momento, puede encontrarse en un determinado programa de lavado
      (que recuerda entre apagados) o puede estar en modo reposo
      (por defecto está en modo reposo).

    Tiene una puerta que puede estar abierta o cerrada
      (por defecto está abierta).

    Tiene un depósito para el detergente y otro para el suavizante,
      con una capacidad de 3 litros y 5 litros, respectivamente.

    Los programas de lavado se identifican mediante un número del 0 al 4,
      con el siguiente significado:

    0: modo reposo (representa que no está en ningún programa de lavado).
    1: prelavado.
    2: lavado.
    3: aclarado.
    4: centrifugado.

    La lavadora va pasando por todos los programas de lavado desde el
      actual hasta el último (si no está ya en modo reposo),
      y acaba siempre en modo reposo. Por ejemplo, si se empieza desde
      el programa 1, pasaría por los programas 1 flecha derecha 2
      flecha derecha 3 flecha derecha 4 flecha derecha 0.
      Si empieza por el 2, pasaría por 2 flecha derecha 3 flecha derecha 4
      flecha derecha 0.

    Los depósitos deben ser instancias de la clase Deposito.
      El constructor de la clase recibe un número real que representa
      la capacidad total del depósito (en litros), el cual no puede
      cambiar durante la vida del objeto.

    Además, los depósitos deben responder, al menos, a los siguientes métodos:

    capacidad(): devuelve la capacidad total del depósito en litros.
    restante(): devuelve la cantidad de líquido que queda en el depósito,
      en litros.
    llenar(litros): echa en el depósito la cantidad de litros indicada
      (un número real). Si la cantidad total supera la capacidad del depósito,
      se echará justo hasta llenar completamente el depósito.
      Devuelve el objeto depósito.
    quitar(litros): retira del depósito la cantidad de litros indicada
      (un número real). Si se intenta quitar más litros de los que hay
      actualmente en el depósito, simplemente se vaciará completamente el
      depósito. Devuelve el objeto depósito.
    vaciar(): vacía el depósito. Devuelve el objeto depósito.

    La lavadora debe ser instancia de la clase Lavadora.
      La lavadora debe responder, al menos, a los siguientes métodos:

    detergente(): devuelve el depósito de detergente.
    suavizante(): devuelve el depósito de suavizante.
    encender() / apagar(): enciende / apaga la lavadora. Sólo se puede
      encender si está cerrada y si tiene, al menos, 0.8 litros de detergente
      y 0.5 litros de suavizante. Devuelve el objeto lavadora.
    encendida(): Devuelve True si la lavadora está encendida o False
      si está apagada.
    abrir(): abre la lavadora si es posible. La lavadora no se puede abrir
      si tiene activado algún programa de lavado. En tal caso
      (o si la lavadora ya estaba abierta) no hace nada.
      Devuelve el objeto lavadora.
    cerrar(): cierra la lavadora si no estaba ya cerrada. Devuelve el
      objeto lavadora.
    programa(): devuelve el programa de lavado actual de la lavadora.
    programar(programa): pone la lavadora en el programa indicado.
      Sólo funciona si la lavadora está apagada (si está encendida,
      no hace nada). Devuelve el objeto lavadora.
    continuar_programa(): pasa al siguiente programa de lavado,
      si no estaba ya en modo reposo y si la lavadora está encendida.
      Si el siguiente programa de lavado es el modo reposo,
      apaga automáticamente la lavadora. Cada programa de lavado
      consume 0.4 litros de detergente y 0.2 litros de suavizante.
      Devuelve el objeto lavadora.

    Importante:
    Al principio de cada test, se hace:
    lavadora = Lavadora()
    lavadora.detergente().llenar(2)
    lavadora.suavizante().llenar(1)


    Tests
    print(lavadora.cerrar().programar(3).encender().continuar_programa().programa())
      => 4
    print(lavadora.cerrar().programar(3).encender().continuar_programa().detergente().restante())
      => 1.6
    print(lavadora.programar(3).encender().continuar_programa().programa())
      => 3
    print(lavadora.cerrar().programar(3).continuar_programa().programa())
      => 3
'''
