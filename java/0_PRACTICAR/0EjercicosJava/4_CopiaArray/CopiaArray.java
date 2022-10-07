import java.util.Arrays;

public class CopiaArrayCadena {
    private String[] arr1;

    public CopiaArrayCadena(String[] arr1) {
        this.arr1 = new String[5];
        this.arr1 = Arrays.copyOf(arr1, arr1.length + 2);
    }

    public int tamanyoCopia() {
        int n = this.arr1.length;
        return n;
    }

    @Override
    public String toString() {
        String res = "[";
        for (int i = 0; i < tamanyoCopia(); i++) {
            if (i != tamanyoCopia() - 1) {
                res += this.arr1[i];
                res += ", ";
            } else {
                res += this.arr1[i];
                res += "]";
            }

        }
        return res;
    }

}
