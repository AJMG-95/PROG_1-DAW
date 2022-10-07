import java.util.Arrays;

public class CopiaArray2 {

    public static void main(String[] args) {
        String[] arr = new String[] {"A", "B", "C", "D", "E"};
        int l = arr.length;
        arr = Arrays.copyOf(arr, (l + l/2) );
        String res = "[";
        int pos = 0;
        for (String i : arr) {
            res += i;
            if (pos < arr.length - 1) {
                res += ", ";
            } else {
                res += "]";
            }
            pos ++;
        }
        System.out.println(res);
    }

}
