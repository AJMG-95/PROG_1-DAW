import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double n, m, res = 0.0;
        String oper;

        System.out.println("Introduzca el primer operando.");
        while (!sc.hasNextDouble()) {
            sc.next();
            System.err.println("Entrada incorrecta");
            System.out.println("Introduzca el primer operando.");

        }

        n = sc.nextDouble();

        System.out.println("Introduzca el segundo operando.");
        while (!sc.hasNextDouble()) {
            sc.next();
            System.err.println("Entrada incorrecta");
            System.out.println("Introduzca el segundo operando.");

        }

        m = sc.nextDouble();

        System.out.println("Introduzca la operación.");
        oper = sc.next();

        boolean interruptor = true;

        switch (oper) {
            case "*":
                res = n * m;
                break;
            case "+":
                res = n + m;
                break;
            case "-":
                res = n - m;
                break;
            case "/":
                res = n / m;
                break;
            default:
                System.out.println("Operacion incorrecta.");
                interruptor = false;
                break;
        }
        if (interruptor) {
            System.out.println(res);
        }
        sc.close();
    }

}
