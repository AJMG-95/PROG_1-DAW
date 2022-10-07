import java.util.ArrayList;
import java.util.List;

public class Barras {

    public Barras() {
    }

    public static String barras(List<Integer> l, char n) {
        String res = "";
        int c = 0;

        for (int i : l) {
            res+= String.valueOf(n).repeat(i);
            if (c != l.size() - 1) {
                res += "\n";
            }
            c += 1;
        }

        return res;
    }
}
