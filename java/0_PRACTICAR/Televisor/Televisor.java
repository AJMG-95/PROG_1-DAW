import java.util.HashSet;

public class Televisor {
    boolean encendido;
    int canal;
    int volumen;
    Soporte usb;

    public Televisor() {
        encendido = false;
        canal = 0;
        volumen = 0;
        usb = null;
    }

    public Televisor encender() {
        encendido = true;
        return this;
    }

    public Televisor subirVolumen() {
        if(encendido) {
            volumen = Math.min(volumen + 1, 30);
            }
                
        return this;    
    }

    public Televisor bajarVolumen() {
        if(encendido) {
            volumen = Math.max(volumen - 1, 0);
        }
        return this;
    }

    public int getVolumen() {
        return volumen;
    }

    public Televisor sintonizar(int numero) {
        if(encendido) {
            if(numero < 30 && numero > 0) {
                canal = numero;
            }
        }
    return this;
    }

    public int canal() {
        return canal;
    }

    public Televisor conectar(Soporte soporte) {
        usb = soporte;
        return this;
    }

    public Televisor desconectarSiConectado() {
        if(usb != null) {
            usb = null;
        }
        return this;
    }

    public HashSet<String> reproducirSiConectado() {
        
        if(encendido){
            if(usb != null) {
                return new HashSet<>(usb.playlist());
            }
        }
            return new HashSet<>();
    }

}
