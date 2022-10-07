public class Prpl {
    public static void name(String[] args) {
        int x, y;
        float z;
        x = 25;
        y = (int) 44L;
        z = x + y;

        int a = 5;

        final int w = 6, t = w;
        int p = 5, r = p++;
        final int u = 6, b = u + 1;

        short q = 4;
        short g = (int) 4L;

        {
            int c;
            c = 7;
            c += 1;
            c++;
            c -= 25; // c = c - 25;
            System.out.println(c);
            System.out.println(a);
        }

        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        System.out.println(a);
        System.out.println(w);
        System.out.println(t);
        System.out.println(r);
        System.out.println(b);
        System.out.println(q);
        System.out.println(g);

    }
}
