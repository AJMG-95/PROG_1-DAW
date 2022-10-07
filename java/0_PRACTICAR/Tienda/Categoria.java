import java.util.ArrayList;
import java.util.List;

public class Categoria {
    String nombre;
    List<Producto> productos;

    public Categoria(String nombre) {
        this.nombre = nombre;
        productos = new ArrayList<>();
    }

    public void anyadirProducto(Producto producto) {
        if (!productos.contains(producto)) {
            productos.add(producto);
        }

    }
    
    public List<Producto> getProductos() {
        return productos;
    }

}
