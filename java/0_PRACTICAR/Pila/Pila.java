/* Coleccion de elementos que entran y salen uno detras de otro
y el unico elemento al que se puede acceder es el que está encima de la pila,
que es el último que ha entrado (LIFO)*/

package Pila;

import java.util.LinkedList;

public class Pila<E> {

    private LinkedList<E> elementos;

    public Pila() {
        elementos = new LinkedList<>();
    }

    public void meter(E elemento) {
        //elementos.push(elemento);
        elementos.addFirst(elemento);
    }

    public boolean esVacia() {
        return elementos.isEmpty();
    }

    public E sacar() {
        //return elementos.pop();
        return elementos.removeFirst();
    }

    public E cima() {
        return elementos.getFirst();
    }

}
