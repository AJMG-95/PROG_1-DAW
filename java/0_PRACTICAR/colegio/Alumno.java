import java.util.*;

public class Alumno {
    public String nombre;
    public HashMap<Asignatura, HashMap<Integer, Float>> matricula;

    public Alumno(String nombre) {
        this.nombre = nombre;
        matricula = new HashMap<>();
    }

    public Alumno matricular(Asignatura asignatura) {
        HashMap<Integer, Float> trimestres = new HashMap<>();
        for (int i = 1; i <= asignatura.getTrimestre(); i++) {
            trimestres.put(i, null);
        }
        matricula.put(asignatura, trimestres);
        asignatura.anyadirAlumno(this);
        return this;
    }

    public Alumno setNota(Asignatura asignatura, int trimestre, float nota) {
        if (matricula.containsKey(asignatura)) {
            matricula.get(asignatura).put(trimestre, nota);
        }
        return this;
    }

    public Float media(Asignatura asignatura) {
        Float sumas = 0F;
        Float media = 0F;
        int trimestres = 0;
        if (matricula.containsKey(asignatura)) {
            for (Float notas : matricula.get(asignatura).values()) {
                if (notas == null) {
                    sumas += 0;
                } else {
                    trimestres++;
                    sumas += notas;
                }
            }
        }
        media = sumas / trimestres;
        return media;
    }

    public Float nota(Asignatura asignatura, int trimestre) {
        if (matricula.containsKey(asignatura)) {
            return matricula.get(asignatura).get(trimestre);
        } else {
            return null;
        }
    }

    public boolean aprobada(Asignatura asignatura) {
        if (media(asignatura) >= 5) {
            return true;
        } else {
            return false;
        }
    }

    public void getMatricula() {
        System.out.println(matricula);
    }

}
