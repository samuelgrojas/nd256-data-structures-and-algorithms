## Reasoning Behind Decisions:

- Se utiliza collections.OrderedDict para mantener el orden de uso (de menos a más reciente) y aprovechar sus operaciones move_to_end y popitem que permiten implementar LRU de forma directa y eficiente.
- get(key): si existe, se marca como recientemente usado con move_to_end y se devuelve el valor; si no, se devuelve -1 según la especificación del ejercicio.
- set(key, value): si la clave existe se actualiza y se marca como reciente; si no, se inserta y, si se excede la capacidad, se elimina el elemento menos recientemente usado con popitem(last=False).
- Se añaden anotaciones de tipos para claridad y mantenimiento; los tests incluidos cubren comportamiento estándar, reemplazo por clave nueva y capacidad cero como caso límite.

## Time Efficiency:

- get: O(1) amortizado — búsqueda en OrderedDict y move_to_end son operaciones O(1).
- set: O(1) amortizado — asignación en OrderedDict, move_to_end y popitem son O(1).
- Inicialización y operaciones auxiliares son O(1) por llamada; los tests ejecutan un número fijo de operaciones.

## Space Efficiency:

- Espacio usado: O(capacity) para almacenar hasta capacity pares (clave, valor) en la estructura.
- Overhead adicional por la estructura interna de OrderedDict (punteros/entradas enlazadas) pero sigue siendo proporcional al número de elementos almacenados.
- Caso capacity == 0: el caché no mantiene elementos persistentemente (uso efectivo de espacio ≈ O(1)).
