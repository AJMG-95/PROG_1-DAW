import java.util.Collection;
import java.util.HashSet;

public class Asignatura {
    private int numTrimestre;
    private Collection<Alumno> matriculados;
    public String nombreAsig;

    public Asignatura(String nombre, int numTrimestre) {
        this.nombreAsig = nombre;
        this.numTrimestre = numTrimestre;
        matriculados = new HashSet<>();

    }

    public int getTrimestre() {
        return numTrimestre;
    }

    public void getMatriculados() {
        System.out.println(matriculados);
    }

    public void anyadirAlumno(Alumno alumno) {
        matriculados.add(alumno);
    }

}
