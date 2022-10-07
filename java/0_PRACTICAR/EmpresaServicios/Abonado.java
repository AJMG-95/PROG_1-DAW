import java.util.ArrayList;
import java.util.List;

public class Abonado {

    final private String[] SERVICIOS = {"FIJO", "MOVIL", "INTERNET", "TELEVISION"};

    private List<Servicio> listaServicios;
    private String nomAbonado;


    public Abonado(String nomAbonado, Telefono[] telefonos) {
        if (telefonos == null || telefonos.length == 0) {
            throw new IllegalArgumentException("Lista vacia");
        }
        this.listaServicios = new ArrayList<>();
        for (Telefono i : telefonos) {
            this.listaServicios.add(i);
        }
        this.nomAbonado = nomAbonado;

    }

    public Abonado contratar(Servicio servicio){

        if (servicio instanceof Television && !this.listaServicios.contains(Internet.class)){
            throw new IllegalArgumentException("no tiene Internet");
        }
        this.listaServicios.add(servicio);

        return this;
    }

    public int numServicios(){
        return this.listaServicios.size();
    }

}
