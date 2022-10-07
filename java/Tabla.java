import java.util.Scanner;

public class Tabla {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;

        for (;;) {
            System.out.println("Introduzca el número (entre 0 y 10): ");

            while (!sc.hasNextInt()) {
                sc.next();
                System.err.println("Entrada incorrecta");
                System.out.println("Introduzca el número: ");
            }
            n = sc.nextInt();
            if (n < 0 || n > 10) {
                System.err.println("El número debe estar entre 0 y 10");
            } else {
                break;
            }
        }
        for (int i = 0; i <= 10; i++) {
            System.out.print(n);
            System.out.print(" X ");
            System.out.print(i);
            System.out.print(" = ");
            System.out.print(n * i);
        }

        sc.close();
    }
}
