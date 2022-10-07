public class Principal {
    public static void main(String[] args) {
        Asignatura ingles = new Asignatura("Ingles", 3);
        Asignatura mates = new Asignatura("Matemáticas", 2);
        Alumno juan = new Alumno("Juan Pérez");
        Alumno antonio = new Alumno("Antonio García");

        juan.matricular(ingles).matricular(mates);
        antonio.matricular(mates);
        juan.setNota(ingles, 1, 4.0F).setNota(ingles, 2, 6.0F).setNota(ingles, 3, 8.0F);
        antonio.setNota(mates, 1, 2.5F);

        System.out.println(juan.media(ingles));
        System.out.println(antonio.nota(mates, 2));
        System.out.println(antonio.nota(mates, 1));
        System.out.println(antonio.media(mates));
        System.out.println(juan.aprobada(ingles));

    }
}
