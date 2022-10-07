public class Bombilla {
    int potenciaBombilla;
    String tamanyoBombilla;

    public Bombilla(int potenciaBombilla, String tamanyoBombilla){
        this.potenciaBombilla = potenciaBombilla;
        if(tamanyoBombilla == "P" || tamanyoBombilla == "M")
            this.tamanyoBombilla = tamanyoBombilla;
    }

    public int potencia() {
        return potenciaBombilla;
    }

    public String tamanyo() {
        return tamanyoBombilla;
    }
}
