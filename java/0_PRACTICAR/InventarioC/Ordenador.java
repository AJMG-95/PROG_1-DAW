import java.util.ArrayList;
import java.util.List;

public class Ordenador extends Inventariable implements Ubicacion{

    private List<Componente> componentes;

    public Ordenador (Ubicacion ubicacion){
        super(ubicacion);
        this.componentes = new ArrayList<>();
        setUbicacion(ubicacion);
    }

    @Override
    protected void setUbicacion(Ubicacion ubicacion) {
        if (ubicacion instanceof Aula || ubicacion instanceof Armario) {
            this.ubicacion = ubicacion;
        } else{
            throw new IllegalArgumentException("La ubicación no es valida.");
        }
    }

    protected void anyadirComponente(Componente componente){
        componentes.add(componente);
    }

    @Override
    public void baja(){
        super.baja();
        for(Componente c : this.componentes){
            c.baja();
        }
    }
}
