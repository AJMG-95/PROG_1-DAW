import java.util.ArrayList;
import java.util.List;

public class Soporte {

    private List<String> multimedia;

    public Soporte(List<String> multimedia){
        this.multimedia = new ArrayList<>(multimedia);
    }

    public List<String> playList(){
        return this.multimedia;
    }

    public String reproducir(int indice){
        return this.multimedia.get(indice);
    }
}
