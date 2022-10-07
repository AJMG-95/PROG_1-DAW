public class bucles {
    public static void main(String[] args) {
        int x;
        x = 0;
        while (x < 10) {
            System.out.println(x);
            x++;
        }


        int total = 0;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.println(i + j);
                total++;
            }
        }
        System.out.print("El total es: ");
        System.out.println(total);

    }

}
