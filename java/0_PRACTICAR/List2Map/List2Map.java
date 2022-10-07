package PRACTICAR.List2Map;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class List2Map {
    public static void main(String[] args) {

        List<Character> l = List.of('a', 'b', 'c');
        Map<Integer, Character> m = list2map(l);

        for (Integer i : m.keySet()) {
            System.out.println(String.format("%d => %C", i, m.get(i)));
        }

        for (Integer i : m.keySet()) {
            System.out.println(i + "=>" + m.get(i));
        }
    }

    public static <E> Map<Integer, E> list2map(List<E> lista) {
        Map<Integer, E> res = new LinkedHashMap<>();

        for (int i = 0; i < lista.size(); i++) {
            res.put(i, lista.get(i));
            res.put(i - lista.size(), lista.get(i));
        }

        return res;
    }
}
