package ColaPrioridad;

import java.util.LinkedList;

public class ColaPrioridad {
    private LinkedList<Prioritario> elementos;

    public ColaPrioridad() {
        this.elementos = new LinkedList<>();
    }

    public boolean esVacia() {
        return elementos.isEmpty();
    }

    public void meter(Prioritario elemento) {
        int prioridad = elemento.getPrioridad();

        for (int i = 0; i < elementos.size(); i++) {
            if (elementos.get(i).getPrioridad() > prioridad) {
                elementos.add(i, elemento);
                return;
            }

        }

        elementos.addLast(elemento);

    }

    public Prioritario sacar() {
        return elementos.removeFirst();
    }

    public Prioritario primero() {
        return elementos.getFirst();
    }

    public Prioritario ultimo() {
        return elementos.getLast();
    }
}
