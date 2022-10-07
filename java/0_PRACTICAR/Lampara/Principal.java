public class Principal {
    public static void main(String[] args) {
        Bombilla bombilla =  new Bombilla(10, "P");
        Lampara lampara = new Lampara(3, 0, 20);
        Bombilla bombilla2 = new Bombilla(10, "M");

        //System.out.println(lampara.poner(bombilla).potenciaTotal());
        System.out.println(lampara.poner(bombilla2).potenciaTotal());
        //System.out.println(lampara.poner(bombilla).poner(bombilla2).quitar("M").tamanyo());
        //System.out.println(new Lampara(3, 2, 20).poner(new Bombilla(10, "P")).poner(new Bombilla(10, "M").tamanyo()));
        //System.out.println(new Lampara(3, 2, 20).poner(new Bombilla(10, "P")).poner(new Bombilla(10, "M")).quitar("M").tamanyo());
    }
}
