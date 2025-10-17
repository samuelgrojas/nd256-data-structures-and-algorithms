### Union Function

## Reasoning Behind Decisions:

- Se modela la lista enlazada con clases Node y LinkedList para encapsular operaciones básicas (append, size, representación).  
- Para union e intersection se usan sets para deduplicar y calcular la unión/intersección de manera sencilla y eficiente, evitando recorridos repetidos o comparaciones O(n^2).
- La función union: recoge todos los valores únicos de ambas listas y construye una nueva LinkedList con esos valores.  
- La función intersection: construye sets a partir de cada lista y calcula la intersección; luego convierte el conjunto resultante en una LinkedList.
- Consideraciones de diseño: solución clara y didáctica; el uso de sets sacrifica el orden original de los elementos (la salida tiene orden arbitrario). Si se requiere preservar orden, habría que iterar y añadir respetando la primera aparición.

## Time Efficiency:

- Recorrer cada lista para llenar sets: O(n1 + n2) donde n1 y n2 son longitudes de las listas de entrada.
- Operaciones de set (inserción y cálculo de intersección): O(1) amortizado por elemento, por lo que la etapa de conjuntos es O(n1 + n2).
- Construcción de la LinkedList de salida (iterar sobre los elementos del set): O(k), con k número de elementos únicos (k ≤ n1 + n2).
- En resumen: tiempo total O(n1 + n2) amortizado.

## Space Efficiency:

- Uso adicional de memoria: O(k) para los sets y O(k) para la lista de salida (k = número de elementos únicos en la unión o intersección).
- Overhead: nodos adicionales en la LinkedList resultante y estructuras internas de los sets.
- Caso límite: si ambas listas están vacías, coste espacial extra ≈ O(1). Si suffix (no aplica aquí) o estructura con muchos duplicados, k puede ser mucho menor que n1 + n2, reduciendo el uso de memoria.

### Intersection Function

## Reasoning Behind Decisions:

- Se modela la lista enlazada con clases Node y LinkedList para encapsular operaciones básicas (append, size, representación).  
- Para union e intersection se usan sets para deduplicar y calcular la unión/intersección de manera sencilla y eficiente, evitando recorridos repetidos o comparaciones O(n^2).
- La función union: recoge todos los valores únicos de ambas listas y construye una nueva LinkedList con esos valores.  
- La función intersection: construye sets a partir de cada lista y calcula la intersección; luego convierte el conjunto resultante en una LinkedList.
- Consideraciones de diseño: solución clara y didáctica; el uso de sets sacrifica el orden original de los elementos (la salida tiene orden arbitrario). Si se requiere preservar orden, habría que iterar y añadir respetando la primera aparición.

## Time Efficiency:

- Recorrer cada lista para llenar sets: O(n1 + n2) donde n1 y n2 son longitudes de las listas de entrada.
- Operaciones de set (inserción y cálculo de intersección): O(1) amortizado por elemento, por lo que la etapa de conjuntos es O(n1 + n2).
- Construcción de la LinkedList de salida (iterar sobre los elementos del set): O(k), con k número de elementos únicos (k ≤ n1 + n2).
- En resumen: tiempo total O(n1 + n2) amortizado.

## Space Efficiency:

- Uso adicional de memoria: O(k) para los sets y O(k) para la lista de salida (k = número de elementos únicos en la unión o intersección).
- Overhead: nodos adicionales en la LinkedList resultante y estructuras internas de los sets.
- Caso límite: si ambas listas están vacías, coste espacial extra ≈ O(1). Si suffix (no aplica aquí) o estructura con muchos duplicados, k puede ser mucho menor que n1 + n2, reduciendo el uso de memoria.

## Notas / Limitaciones:

- El orden de los elementos en las listas devueltas no está garantizado debido al uso de sets. Para mantener orden de aparición sería mejor iterar las listas y añadir elementos a la salida sólo si no están ya presentes (manteniendo un set auxiliar para control de duplicados).
- Si los elementos no son hashables, habría que usar otra estrategia (por ejemplo, listas y búsqueda explícita), con impacto en la complejidad.
- Implementación robusta y apropiada para entradas típicas donde los valores son enteros hashables y el orden no es crítico.
