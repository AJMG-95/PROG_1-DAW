import java.util.ArrayList;
import java.util.List;

public class Categoria {
    private String denom;
    private List<Producto> productos;

    public Categoria(String denom) {
        this.denom = denom;
        this.productos = new ArrayList<Producto>();
    }

    public void anyadirProducto(Producto producto) {
        this.productos.add(producto);
    }

    public String getDenom() {
        return this.denom;
    }

    public void setDenom(String denom) {
        this.denom = denom;
    }

    public List<Producto> getProductos() {
        return new ArrayList<>(this.productos);
    }

}
