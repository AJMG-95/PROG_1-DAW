import java.util.List;

public class Barras {

    public Barras() {

    }

    public static String barras(List<Integer> lista, char caracter) {
        String resultado = "";
        for (int i : lista) {
            resultado += String.valueOf(caracter).repeat(i);
            resultado += "\n";
        }
        resultado = resultado.substring(0, resultado.length() - 1);
        return resultado;
    }

}
