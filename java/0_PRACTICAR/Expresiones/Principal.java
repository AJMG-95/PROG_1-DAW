public class Principal {
    public static void main(String[] args) {
    
        System.out.println(new Numero(2).valor());
        System.out.println(new Suma(new Numero(2), new Producto(new Numero(3), new Numero(5))).valor());
        System.out.println(new Producto(new Numero(2), new Suma(new Numero(3), new Numero(5))).valor());
}   
}
