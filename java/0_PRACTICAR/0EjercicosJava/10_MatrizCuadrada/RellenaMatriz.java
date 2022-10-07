public class RellenaMatriz {
    public static void main(String[] args) {
        int n = 3;
        int[][] matriz = new int[n][n];

        if ( n < 0){
            throw new RuntimeException("El valor no debe ser negativo");
        }

        for (int i = 0; i < n; i++) {
            for (int e = 0; e < n; e++) {
                matriz[i][e] = n;
            }
        }


        for (int[] i : matriz) {
            for (int e : i) {
                System.out.print(e);
            }
            System.out.println();
        }
    }


}
