public class Producto {

    private int id;
    private String nombre;
    private double precio;
    private Categoria categoria;

    public Producto(int id, String nombre, double precio, Categoria categoria) {
        this.id = id;
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
        categoria.anyadirProducto(this);
    }

}
