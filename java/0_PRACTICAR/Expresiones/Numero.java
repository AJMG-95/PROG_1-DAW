public class Numero extends Expresion {
    int x;

    public Numero(int x) {
        this.x = x;
    }

    @Override
    public int valor() {
        return x;
    }
}
