import java.util.ArrayList;
import java.util.List;

public abstract class Inventariable {

    protected Ubicacion ubicacion;
    private List<Ubicacion> historico;

    protected abstract void setUbicacion(Ubicacion ubicacion);

    protected Inventariable(Ubicacion ubicacion) {
        if (ubicacion == null) {
            throw new IllegalArgumentException("Falta la ubicación");
        }

        this.historico = new ArrayList<>();
        this.historico.add(ubicacion);
    }

    public Ubicacion ubicacion() {
        return this.ubicacion;
    }

    public Inventariable mover(Ubicacion nuevaUbicacion) {
        if (nuevaUbicacion == null) {
            throw new IllegalArgumentException("Está de baja y no se puede mover");
        }
        setUbicacion(nuevaUbicacion);
        this.historico.add(nuevaUbicacion);
        return this;
    }

    public List<Ubicacion> historico() {
        return new ArrayList<>(this.historico);
    }

    public void baja() {
        this.ubicacion = null;
    }

}
