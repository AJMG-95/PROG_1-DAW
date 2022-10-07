public class Internet implements Servicio {

    private String puntoDeServicio;


    public Internet(String puntoDeServicio) {
        this.puntoDeServicio = puntoDeServicio;
    }


    public String getPuntoDeServicio() {
        return this.puntoDeServicio;
    }


}
