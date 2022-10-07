import java.util.ArrayList;
import java.util.List;

public class Categoria {

    private String nombre;
    private List<Producto> productos;

    public Categoria(String nombre) {
        this.nombre = nombre;
        this.productos = new ArrayList<>();
    }

    protected String getNombre() {
        return this.nombre;
    }

    protected void anyadirProducto(Producto producto) {
        this.productos.add(producto);
    }

    public List<Producto> getProductos() {
        return new ArrayList<>(this.productos);
    }
}
