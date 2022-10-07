import java.util.HashMap;
import java.util.Map;

public class Carrito {

    private Map<Producto, Integer> productos;

    public Carrito() {
        this.productos = new HashMap<Producto, Integer>();
    }

    public void anyadirProducto(Producto producto) {
        if (this.productos.containsKey(producto)) {
            this.productos.put(producto, productos.get(producto) + 1);
        } else {
            this.productos.put(producto, 1);
        }

    }

    public void anyadirNProducto(Producto producto, int n) {
        if (this.productos.containsKey(producto)) {
            this.productos.put(producto, productos.get(producto) + n);
        } else {
            this.productos.put(producto, n);
        }

    }

    public void quitarProducto(Producto producto){
        if (this.productos.get(producto) - 1 > 0) {
            this.productos.put(producto, productos.get(producto) - 1);
        }
        if (this.productos.get(producto) - 1 == 0) {
            this.productos.remove(producto);
        }
    }

    public void quitarNProducto(Producto producto, int n){
        if (this.productos.get(producto) - n > 0) {
            this.productos.put(producto, productos.get(producto) - n);
        } else if (this.productos.get(producto) - n == 0) {
            this.productos.remove(producto);
        } else {
            throw new IllegalArgumentException("No puede retirar una cantidad superior que la contenida en el carrito.");
        }
    }

    public void vaciar() {
        this.productos.clear();
    }

    public Map<Producto, Integer> getEntradas() {
        return this.productos;
    }

}
