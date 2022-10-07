public class Polinomio {

    private int[] coeficientes;

    public Polinomio(int[] coeficintes) {
        this.coeficientes = coeficintes;
    }

    @Override
    public String toString() {
        String resultado = "";
        int tamanyo = this.coeficientes.length;

        if (tamanyo == 1 && coeficientes[0] == 0) {
            return "0";
        }
        for (int i = 0; i < tamanyo; i++) {
            if (this.coeficientes[i] == 0 && i < tamanyo - 1) {
                continue;
            }

            if (i > 0 && this.coeficientes[i] > 0) {
                resultado += "+";
            }
            if (i == tamanyo - 1 && this.coeficientes[i] != 0) {
                resultado += (String.valueOf(this.coeficientes[i]));
            } else if (i < tamanyo - 2) {
                resultado += (String.valueOf(this.coeficientes[i]) + "x^" + String.valueOf(tamanyo - (i + 1)));
            } else if (i == tamanyo - 2) {
                resultado += (String.valueOf(this.coeficientes[i]) + "x");
            }
        }
        return resultado;
    }

    public Polinomio derivada() {
        int tamanyo = this.coeficientes.length;
        int[] derivada = new int[tamanyo - 1];

        for (int i = 0; i < tamanyo - 1; i++) {
            int res = this.coeficientes[i] * (tamanyo - (i + 1));
            derivada[i] = res;
        }

        return new Polinomio(derivada);
    }
}
