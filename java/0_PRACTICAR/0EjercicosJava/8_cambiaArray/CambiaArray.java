import java.util.*;

public class CambiaArray {


    public static void main(String[] args) {
        int[] arr1 = new int[] {1, 2, 3};
        cambiar(arr1);
        cambiar2(arr1);
        final int[] arr2 = new int[] {4, 5, 6};
        cambiar(arr2);
        cambiar2(arr2);

        for (int i: arr1){
         System.out.println(i);
        }
        for (int i: arr2){
            System.out.println(i);
        }


    }

    public static void cambiar(int[] arr) {
        arr[0] = 0;
    }

    final public static void cambiar2(int[] arr) {
        arr[1] = 13;
    }
}
