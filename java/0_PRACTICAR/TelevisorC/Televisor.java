import java.util.HashSet;
import java.util.List;

import org.w3c.dom.ranges.Range;

public class Televisor {

    private boolean encendido;
    private int canal;
    private int volumen;
    private Soporte soporte;


    public Televisor() {
        this.encendido = false;
        this.canal = 1;
        this.volumen = 0;
        this.soporte = null;
    }

    public Televisor encender(){
        this.encendido = true;
        return this;
    }

    public Televisor apagar(){
        this.encendido = false;
        return this;
    }

    public Integer getVolumen(){
        return this.volumen;
    }
    public Televisor subirVolumen(){
        if (this.encendido && this.getVolumen() < 30) {
            this.volumen += 1;
        }

        return this;
    }

    public Televisor bajarVolumen() {
        if (this.encendido && this.getVolumen() > 0) {
            this.volumen -= 1;
        }

        return this;
    }

    public Televisor sintonizar(int canal){
        if (this.encendido && 0 < canal && 100 >= canal) {
            this.canal = canal;
        }
        return this;
    }

    public int canal(){
        return this.canal;
    }

    public Televisor conectar(Soporte soporte) {
        this.soporte = soporte;
        return this;
    }

    public Televisor desconectarSiConectado(){
        this.soporte = null;
        return this;
    }

    public HashSet<String> reproducirSiConectado() {
        if (this.encendido && this.soporte != null) {
            return new HashSet<String>(soporte.playList());
        }
        return new HashSet<String>();
    }



}
