public class ArrayMixta {
    public static void main(String[] args) {
        Object[] arr = new Object[] {
            1,
            "El Pepe",
            true,
            null,
            new StringBuilder()
        };

        mostrar(arr);
    }

    public static void mostrar(Object[] arr){
        for (Object i : arr) {
            System.out.println(i);
        }
    }
}
