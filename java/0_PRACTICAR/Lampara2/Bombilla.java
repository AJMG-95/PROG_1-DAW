package EXAMANES_P_A_J.LampBomb;

public class Bombilla {
    /*
     * public enum Tamanyo {
     * PEQUENYO("P"), MEDIANO("M");
     * 
     * private String abreviatura;
     * 
     * private Tamanyo(String abreviatura) {
     * this.abreviatura = abreviatura;
     * }
     * 
     * public String getAbreviatura() {
     * return abreviatura;
     * }
     * }
     */

    private float potencia;
    private Tamanyo tamanyo;

    public Bombilla(float potencia, Tamanyo tamanyo) {
        // if (!List.of(Tamanyo.PEQUENYO, Tamanyo.MEDIANO).contains(tamanyo)) {
        // throw new IllegalArgumentException("Tamaño incorrecto");
        // }
        this.potencia = potencia;
        this.tamanyo = tamanyo;
    }

    public float getPotencia() {
        return potencia;
    }

    public Tamanyo getTamanyo() {
        return tamanyo;
    }
}
