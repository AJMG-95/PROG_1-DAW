import java.util.Scanner;

public class SumaEnteros {

    public static void main(String[] args) {
        int [] arr = new int[5];
        Scanner sc = new Scanner(System.in);
        int res = 0;
        int indice = 0;
        System.out.println("Introduce 5 enteros.");

        while (!sc.hasNextLine()) {
            sc.next();
        }

        while (indice != arr.length){
            arr[indice] = sc.nextInt();
            indice++;
        }

        System.out.println("-------");

        for (int i : arr) {
            System.out.println(i);
            res += i;
        }

        System.out.print("La suma es: ");

        System.out.println(res);
    }
}
