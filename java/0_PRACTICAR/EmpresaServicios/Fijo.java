public class Fijo extends Telefono implements Servicio {

    private String puntoDeServicio;


    public Fijo(long n, String puntoDeServicio) {
        super(n);
        this.puntoDeServicio = puntoDeServicio;
    }

    public String getPuntoDeServicio() {
        return this.puntoDeServicio;
    }


}
