public class RellenaMatriz2 {

    private int[][] matriz;



    public int[][] rellenaCuadrado(int n){
        if ( n < 0){
            throw new RuntimeException("El valor no debe ser negativo");
        }

        this.matriz = new int[n][n];

        for (int i = 0; i < n ; i++) {
            for (int e = 0; e < n; e++) {
                this.matriz[i][e] = n;
            }
        }

        return matriz;
    }

    @Override
    public String toString() {
        String res = "";
        String c1 = "[";
        String c2 = "]";
        String c3 = ", ";
        int cont = 0;

        for (int[] i : this.matriz) {
            res += c1;
            res += c1;
            for (int e = 0; e < i.length ; e++) {
                res += e;
                if (e != i.length - 1) {
                    res += c3;
                }
            }
            res+= c2;
            cont += 1;
            if (cont != this.matriz.length - 1) {
                res += c3;
            }

        }
        return res;
    }
}
