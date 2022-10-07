import java.util.ArrayList;
import java.util.List;

public class Lampara {
    List<Bombilla> lamparaPequenios;
    List<Bombilla> lamparaMedianos;
    int potenciaMax;
    int potencia;
    int casquillosPequenios;
    int casquillosMedianos;
    int casquillosPusados;
    int casquillosMusados;

    public Lampara(int casquillosPequenios, int casquillosMedianos, int potenciaMax) {
        lamparaPequenios = new ArrayList<>();
        lamparaMedianos = new ArrayList<>();
        this.casquillosMedianos = casquillosMedianos;
        this.casquillosPequenios = casquillosPequenios;
        this.potenciaMax = potenciaMax;
        casquillosPusados = 0;
        casquillosMusados = 0;
        potencia = 0;
    }

    public Lampara poner(Bombilla bombilla) {
        if((potencia + bombilla.potencia()) <= potenciaMax) {
            if(bombilla.tamanyo() == "P" && casquillosPequenios > casquillosPusados + 1) {
                lamparaPequenios.add(bombilla);
                casquillosPusados += 1;
                potencia += bombilla.potencia();
            }
            if(bombilla.tamanyo() == "M" && casquillosMedianos > casquillosMusados + 1) {
                lamparaMedianos.add(bombilla);
                casquillosMusados += 1;
                potencia += bombilla.potencia();
            }
        }

        return this;
    }
    
    public Bombilla quitar(String tamanyo) {
        Bombilla bombilla;
        bombilla = null;
        if(tamanyo == "P" && (lamparaPequenios.size() != 0)) {
            bombilla = lamparaPequenios.get(0);
            lamparaPequenios.remove(0);
            casquillosPusados -= 1;
        }
        if(tamanyo == "M" && (lamparaMedianos.size() != 0)) {
            bombilla = lamparaMedianos.get(0);
            lamparaMedianos.remove(0);
            casquillosPusados -= 1;
        }
        return bombilla;
    }

    public int potenciaTotal() {
        return potencia;
    }

    }
