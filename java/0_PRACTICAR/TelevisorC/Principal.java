import java.util.HashSet;
import java.util.List;
public class Principal {
    public static void main(String[] args) {
        Soporte soporte = new Soporte(List.of("The Batman.mp4", "Superman.mp4"));
        System.out.println((new Televisor()).encender().bajarVolumen().getVolumen());
        System.out.println((new Televisor()).subirVolumen().encender().subirVolumen().getVolumen());
        System.out.println((new Televisor()).conectar(soporte).reproducirSiConectado().equals(new HashSet<String>()));
        System.out.println((new Televisor()).conectar(soporte).encender().reproducirSiConectado().equals(new HashSet<String>(List.of("The Batman.mp4", "Superman.mp4"))));
    }
}
