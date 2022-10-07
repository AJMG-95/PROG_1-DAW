public class Puerta {

    private String color;
    private boolean abierta;
    private Llave llave;

    public Puerta(String color){
        this.color = color;
        this.abierta = false;
        this.llave = null;

    }

    private String getColor(){
        return this.color;
    }

    public Puerta poner(Llave llave){
        this.llave = llave;
        return  this;
    }

    public Llave quitar(){
        Llave l = this.llave;
        this.llave = null;
        return l;
    }

    public boolean abrir(){
        if (this.llave != null &&
            llave.getColor().equals(this.getColor()) ){
                this.abierta = true;
            }
        return this.abierta;
    }

    public void cerrar(){
        this.abierta = false;
    }
}
