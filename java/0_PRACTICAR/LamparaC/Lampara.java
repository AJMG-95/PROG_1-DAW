import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Lampara {

    private Map<String, Integer> casquillos;
    private Map<String, List<Bombilla>> bombillas;
    private int potenciaMaxima;

    public Lampara(int cp, int cm, int potenciaMaxima) {
        setUpCasquillo(cp, cm);
        setUpBombilla();
        this.potenciaMaxima = potenciaMaxima;
    }

    private void setUpCasquillo(int cp, int cm) {
        this.casquillos = new HashMap<String, Integer>();
        this.casquillos.put("P", cp);
        this.casquillos.put("M", cm);
    }

    private void setUpBombilla() {
        this.bombillas = new HashMap<String, List<Bombilla>>();
        this.bombillas.put("P", new ArrayList<Bombilla>());
        this.bombillas.put("M", new ArrayList<Bombilla>());
    }

    public int potencia_total() {
        int res = 0;
        for (String clave : this.bombillas.keySet()) {
            List<Bombilla> listaBombillas = this.bombillas.get(clave);
            for (Bombilla b : listaBombillas) {
                res += b.getPotencia();
            }
        }
        return res;
    }

    public Lampara poner(Bombilla bombilla) {
        String tamBombilla = bombilla.getTamanyo();
        if ((this.bombillas.get(tamBombilla).size() < this.casquillos.get(tamBombilla)) &&
            (this.potencia_total() + bombilla.getPotencia() <= this.potenciaMaxima)) {
                this.bombillas.get(tamBombilla).add(bombilla);
            }
        return this;
    }

    public Bombilla quitar(String tamanyo) {
        if (this.bombillas.get(tamanyo).isEmpty()){
            return null;
        }
        Bombilla bomQuitada = this.bombillas.get(tamanyo).get(0);
        this.bombillas.get(tamanyo).remove(0);
        return bomQuitada;
    }

}
