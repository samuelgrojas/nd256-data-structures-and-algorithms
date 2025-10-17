## Reasoning Behind Decisions:

- Se usa collections.defaultdict para contar frecuencias de caracteres de forma simple y segura.
- heapq (min-heap) para construir la cola de prioridad y combinar nodos según frecuencia; la clase HuffmanNode define __lt__ para que heapq compare por freq.
- HuffmanNode almacena char, freq y referencias left/right; la construcción del árbol une los dos nodos de menor frecuencia hasta obtener la raíz.
- Generación de códigos mediante recorrido recursivo del árbol (generate_huffman_codes). Se gestiona el caso especial de un único carácter asignando un código no vacío ("0") para que el encoding/decoding funcione correctamente.
- Codificación: se crea el string codificado concatenando los códigos de cada caracter en el texto original.
- Decodificación: se recorre el árbol según los bits y se añade el carácter al alcanzar una hoja; se contempla el caso de árbol nulo y el de árbol con un solo nodo.

## Time Efficiency:

- Calcular frecuencias: O(n) donde n es la longitud del texto.
- Construcción del heap inicial: O(k) para heapify (k = número de caracteres únicos).
- Construcción del árbol Huffman: O(k log k) por las operaciones de extracción/ inserción en la heap al combinar nodos.
- Generación de códigos (recorrido del árbol): O(k).
- Codificación del texto original usando los códigos: O(n).
- Decodificación: O(m) donde m es la longitud en bits del texto codificado (m ≤ n * max_code_len); en práctica O(n) respecto al número de símbolos decodificados.
- En resumen: dominante O(n + k log k).

## Space Efficiency:

- Estructuras principales: O(k) para el árbol y el diccionario de códigos (k = número de símbolos distintos).
- Espacio para la salida codificada: O(m) (longitud en bits del resultado); m depende de las frecuencias y longitudes de código (en el peor caso O(n log k)).
- Memoria auxiliar constante aparte de la pila de recursion en generate_huffman_codes (profundidad ≤ k).
- Casos especiales: entrada vacía retorna cadena vacía; un único carácter produce árbol con un nodo y codificación de longitud n con un código fijo (se evita código vacío con la solución implementada).
