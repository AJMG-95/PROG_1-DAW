import java.util.*;

public class Soporte {
    List<String> playlist;


    public Soporte(List<String> playlist) {
        this.playlist = new ArrayList<>(playlist);
    }

    public List<String> playlist() {
        return playlist;
    }

    public String reproducir(int indice) {
        return playlist.get(indice);
    }
}
