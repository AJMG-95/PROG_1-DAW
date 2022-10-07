public class Componente extends Inventariable {
    private String nombre;

    public Componente(String nombre, Ubicacion ubicacion) {
        super(ubicacion);
        this.nombre = nombre;
        setUbicacion(ubicacion);
    }

    @Override
    protected void setUbicacion(Ubicacion ubicacion) {
        // if (ubicacion.getClass() == Aula.class){}
        if (!(ubicacion instanceof Ordenador || ubicacion instanceof Armario)) {
            throw new IllegalArgumentException("Ubicación no valida");
        }

        if (ubicacion instanceof Ordenador) {
            Ordenador O = (Ordenador) ubicacion;
            O.anyadirComponente(this);
        }

        this.ubicacion = ubicacion;
    }

    public String getNombre() {
        return this.nombre;
    }

}
