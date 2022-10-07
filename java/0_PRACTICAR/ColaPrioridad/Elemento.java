package ColaPrioridad;

public class Elemento<E> implements Prioritario {
        private int prioridad;
        private E info;

        public Elemento(int prioridad, E info) {
                this.prioridad = prioridad;
                this.info = info;
        }

        @Override
        public int getPrioridad() {
                return this.prioridad;
        }

        public E getInfo() {
                return this.info;
        }

}
