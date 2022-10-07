public class Principal {
    public static void main(String[] args) {
        System.out.println(new Puerta("rojo").poner(new Llave("rojo")).abrir() == true);
        System.out.println(new Puerta("rojo").poner(new Llave("verde")).abrir() == false);
        System.out.println(new Puerta("rojo").abrir() == false);

    }
}
