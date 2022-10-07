public class Matriz {
   public static void main(String[] args) {
    int[][] matriz = new int[][]{{1, 2 , 3},{4, 5, 6},{7, 8, 9}};

    for(int[] i : matriz){
        for (int e : i){
            System.out.print(e);
        }
        System.out.println();
    }
   }
}
