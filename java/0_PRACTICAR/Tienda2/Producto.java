public class Producto {
    private int cod;
    private String denom;
    private double precio;
    private Categoria cat;

    public Producto(int cod, String denom, double precio, Categoria cat) {
        this.cod = cod;
        this.denom = denom;
        this.precio = precio;
        this.cat = cat;
        this.cat.anyadirProducto(this);
    }

}
