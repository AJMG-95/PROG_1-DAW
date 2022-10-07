public class Cuadrado {

    private int n;
    private int[][] matriz;


    public Cuadrado(int n) {
        this.n = n;
        this.matriz = new int[n][n];
    }


    public static int[][] cuadrado(int n) {
        int [][] matriz = new int[n][n];

        if ( n < 0){
            throw new RuntimeException("El valor no debe ser negativo");
        }

        for (int i = 0; i == n; i++) {
            for (int e = 0; e == n; e++) {
                matriz[i][e] = n - (n - (i + 1));
            }

        }

        return matriz;
    }

}
