public class Producto {
    private int codigo;
    private String denominacion;
    private Double precio;
    private Categoria categoria;

    public Producto(int codigo, String denominacion, Double precio, Categoria categoria) {
        this.codigo = codigo;
        this.denominacion = denominacion;
        this.precio = precio;
        this.categoria = categoria;
        categoria.anyadirProducto(this);
    }

    public int getCodigo() {
        return this.codigo;
    }

    public String getDenominacion() {
        return this.denominacion;
    }

    public Double getPrecio() {
        return this.precio;
    }

    public Categoria getCategoria() {
        return this.categoria;
    }

}
