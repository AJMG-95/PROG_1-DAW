package Pila;

public class Principal {

    public static void main(String[] args) {
        Pila<Integer> p = new Pila<>();
        System.out.println(p.esVacia());
        p.meter(5);
        p.meter(6);
        System.out.println(p.cima());
        p.sacar();
        System.out.println(p.cima());

    }


}
