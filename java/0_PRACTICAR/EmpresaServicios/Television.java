public class Television implements Servicio {

    private String puntoDeServicio;


    public Television(String puntoDeServicio) {
        this.puntoDeServicio = puntoDeServicio;
    }


    public String getPuntoDeServicio() {
        return this.puntoDeServicio;
    }


}
