public class Par {
    public static void main(String[] args) {
        int x = (int) (Math.random() * 100);

        System.out.print("La x vale: ");
        System.out.println(x);

        if (x % 2 == 0) {
            System.out.println("La x es par.");
        } else {
            System.out.println("La x es impar");
        }

        switch (x % 2) {
            case 0:
                System.out.println("La x es par.");
                break;
            case 1:
                System.out.println("La x es par.");
                break;

        }
    }
}
