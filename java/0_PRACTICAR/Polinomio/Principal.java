public class Principal {
    public static void main(String[] args) {
        // System.out.println(new Polinomio(new int[] {}));
        System.out.println(new Polinomio(new int[] { 3 }));
        System.out.println(new Polinomio(new int[] { 0 }));
        System.out.println(new Polinomio(new int[] { 3, 4 }));
        System.out.println(new Polinomio(new int[] { 3, 4, -3 }));
        System.out.println(new Polinomio(new int[] { 3, 4, 0 }));
        System.out.println(new Polinomio(new int[] { 3, 0, 2, 5 }));
        System.out.println(new Polinomio(new int[] { 9, 3, 0, 2, 5 }));
        System.out.println(new Polinomio(new int[] { 3, 4, 6, 5, 6, 7 }));
        System.out.println("Derivadas:");
        // System.out.println((new Polinomio(new int[] { 4 })).derivada());
        System.out.println((new Polinomio(new int[] { 3, 4 })).derivada());
        System.out.println((new Polinomio(new int[] { 3, 4, -3 })).derivada());
        System.out.println((new Polinomio(new int[] { 3, 0, 2, 5 })).derivada());

    }
}
