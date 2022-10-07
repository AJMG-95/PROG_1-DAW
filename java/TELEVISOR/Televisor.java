package TELEVISOR;

public class Televisor {
    private int canal = 1;
    private int volumen = 0;
    private boolean encendido = false;
    private Pendrive multimedia;

    public int getCanal() {
        return this.canal;
    }

    public void setCanal(int canal) {
        if (canal >= 1 && canal <= 100) {
            this.canal = canal;
        }
    }

    public int getVolumen() {
        return this.volumen;
    }

    public void setVolumen(int volumen) {
        if (volumen >= 0 && volumen <= 30) {
            this.volumen = volumen;
        }
    }

    public boolean getEncendido() {
        return this.encendido;
    }

    private void setEncendido(boolean encendido) {
        this.encendido = encendido;
    }

    public void encender() {
        this.setEncendido(true);
    }

    public void apagar() {
        this.setEncendido(false);
    }

    public Pendrive getMultimedia() {
        return this.multimedia;
    }

    public void conectar(Pendrive multimedia) {
        this.multimedia = multimedia;
    }

    public void reproducir() {
        String[] contenido;

        if (this.getMultimedia() != null && this.getEncendido()) {
            contenido = this.multimedia.getContenido();

            for (int i = 0; i < contenido.length; i++) {
                System.out.println(contenido[i]);
            }
        }
    }
}

class Pendrive {
    String[] contenido;

    public String[] getContenido() {
        return this.contenido;
    }

    public void setContenido(String[] contenido) {
        this.contenido = contenido;
    }
}
