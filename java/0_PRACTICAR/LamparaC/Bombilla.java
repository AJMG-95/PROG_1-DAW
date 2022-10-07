import java.util.Arrays;

public class Bombilla {

    private final String[] TAMANYOS = new String[]{"P", "M"};
    private String tamanyo;
    private int potencia;

    public Bombilla(int potencia, String tamanyo){
        this.potencia = potencia;
        setTamanyo(tamanyo);
    }

    private void setTamanyo(String tamanyo) {

        if (Arrays.asList(TAMANYOS).contains(tamanyo)) {
            this.tamanyo = tamanyo;
        } else {
            throw new IllegalArgumentException("Tamaño incorrecto");
        }

        // for (String t : TAMANYOS) {
        //     if (!t.equals(tamanyo)) {
        //         throw new IllegalArgumentException("Tamaño incorrecto");
        //     }
        // }
        // this.tamanyo = tamanyo;
    }

    public int getPotencia(){
        return this.potencia;
    }

    public String getTamanyo(){
        return this.tamanyo;
    }
}
