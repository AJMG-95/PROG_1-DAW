import java.util.*;

public class ComparaArrays {
    public static void main(String[] args) {
        String[] arr1 = new String[] {"El Pepe"};
        String[] arr2 = new String[] {"El Pepe"};
        String[] arr3 = new String[] {"La Pepa"};

        boolean retval = Arrays.equals(arr1, arr2);
        System.out.println("arr1 and arr2 equal: " + retval);

        boolean retval2 = Arrays.equals(arr1, arr3);
        System.out.println("arr1 and arr3 equal: " + retval2);

    }
}
