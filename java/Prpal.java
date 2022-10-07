public class Prpal {
    public static void name(String[] args) {
        String s = "Hola";
        String w = s;

        System.out.println(w);

        {
            int x = 5;

            if (x == 5) {
                x++;
                System.out.println("La x vale 6");
            }

            if (x == 7) {
                System.out.println("La x vale 7");
            } else if (x != 7) {
                System.out.println("La x no vale 7");
            }

        }

        {
            int x = 4;

            switch (x) {
                case 4:
                    System.out.println(x);
                    System.out.println("La x vale 4");
                    break;
                case 5:
                    System.out.println(x);
                    System.out.println("La x vale 4");
                    break;
                default:
                    System.out.println(x);
                    System.out.println("La x tiene otro valor");
                    break;
            }


        }
    }

}
