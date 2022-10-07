public class Usuario {

    private Carrito carrito;

    public Usuario(){
        this.carrito = new Carrito();
    }

    protected Carrito getCarrito(){
        return this.carrito;
    }
}
