public class Componente extends Inventariable {

    private String nombre;

    public Componente(String nombre, Ubicacion ubicacion) {
        super(ubicacion);
        this.nombre = nombre;
        setUbicacion(ubicacion);
    }

    @Override
    protected void setUbicacion(Ubicacion ubicacion) {
        if (!(ubicacion instanceof Ordenador || ubicacion instanceof Armario)) {
            throw new IllegalArgumentException("La ubicación no es valida.");

        }

        if (ubicacion instanceof Ordenador) {
            Ordenador ordenador = (Ordenador) ubicacion;
            ordenador.anyadirComponente(this);
        }

        this.ubicacion = ubicacion;
    }
}
