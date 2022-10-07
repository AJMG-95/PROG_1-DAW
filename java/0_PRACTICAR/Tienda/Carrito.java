import java.util.HashMap;
import java.util.Map;

public class Carrito {
    Map<Producto, Integer> entradaCarrito;

    public Carrito() {
        entradaCarrito = new HashMap<Producto, Integer>();
    }

    public void anyadirProducto(Producto producto) {
        int total = 0;
        if (!entradaCarrito.containsKey(producto)) {
            entradaCarrito.put(producto, total + 1);
        } else {
            total = entradaCarrito.get(producto);
            entradaCarrito.put(producto, total + 1);
        }
    }

    public void quitarProducto(Producto producto) {
        int total = entradaCarrito.get(producto);
        if (entradaCarrito.containsKey(producto)) {
            if (total - 1 == 0) {
                entradaCarrito.remove(producto);
            } else {
                entradaCarrito.put(producto, total - 1);
            }
        }
    }

    public void vaciarProducto() {
        entradaCarrito.clear();
    }

    public Map<Producto, Integer> getEntradas() {
        return entradaCarrito;
    }
}
