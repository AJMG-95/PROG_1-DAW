import java.util.HashMap;
import java.util.Map;

public class Carrito {
    private Map<Producto, Integer> productos;

    public Carrito() {
        this.productos = new HashMap<>();
    }

    public Map<Producto, Integer> getEntradas() {
        return this.productos;
    }

    // private int cantidadProducto(Producto producto) {
    // if (!this.productos.containsKey(producto)) {
    // throw new IllegalArgumentException("Producto Inexistente");
    // }

    // return this.productos.get(producto);
    // }

    public void anyadirProducto(Producto producto) {
        if (this.productos.containsKey(producto)) {
            this.productos.put(producto, productos.get(producto) + 1);
        } else {
            this.productos.put(producto, 1);
        }
    }

    public void retirarProducto(Producto producto) {
        int cantidad;

        if (!this.productos.containsKey(producto)) {
            throw new IllegalArgumentException("Producto Inexistente");
        }

        cantidad = this.productos.get(producto);

        if (cantidad > 1) {
            this.productos.put(producto, cantidad - 1);
        } else {
            this.productos.remove(producto);
        }

    }
}
