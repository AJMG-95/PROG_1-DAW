import java.util.ArrayList;
import java.util.List;

public class Ordenador extends Inventariable implements Ubicacion {

    private List<Componente> componentes;

    public Ordenador(Ubicacion ubicacion) {
        super(ubicacion);
        setUbicacion(ubicacion);
        componentes = new ArrayList<>();
    }

    public void anyadirComponente(Componente componente) {
        componentes.add(componente);
    }

    @Override
    protected void setUbicacion(Ubicacion ubicacion) {
        // if (ubicacion.getClass() == Aula.class){}
        if (!(ubicacion instanceof Aula || ubicacion instanceof Armario)) {
            throw new IllegalArgumentException("Ubicación no valida");
        }
        this.ubicacion = ubicacion;
    }

    @Override
    public void baja() {
        super.baja();
        for (Componente c : componentes) {
            c.baja();
        }
    }
}
