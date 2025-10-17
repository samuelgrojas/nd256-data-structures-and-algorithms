## Reasoning Behind Decisions:

- Se modela cada bloque con la clase Block que contiene timestamp, data, previous_hash y el hash calculado (SHA-256) para enlazar bloques y detectar modificaciones.
- El hash se calcula sobre la concatenación de timestamp, data y previous_hash, lo que liga el contenido y el orden de los bloques.
- La clase Blockchain mantiene una lista (chain) y crea un genesis block en la inicialización; add_block añade nuevos bloques usando el hash del último bloque como previous_hash.
- Diseño simple y didáctico: muestra las propiedades básicas de una cadena de bloques (enlace por hash, creación de bloques, verificación básica) sin mecanismos avanzados como proof-of-work o firmas.

## Time Efficiency:

- Cálculo del hash por bloque: O(L) donde L es la longitud de los datos y representación del timestamp (coste lineal en tamaño del contenido).
- Añadir un bloque (add_block): O(1) amortizado para append + coste O(L) para calcular el hash.
- Verificación completa de la integridad (recorrer la cadena comprobando previous_hash): O(n) donde n es el número de bloques.
- Operaciones de representación (__repr__): O(n * avg_block_repr) para construir la cadena de texto.

## Space Efficiency:

- Espacio para la cadena: O(n) bloques almacenados en la lista chain.
- Cada bloque ocupa espacio O(L_block) (timestamp, datos y hash); el tamaño del hash es constante (digest SHA-256).
- Overhead adicional: estructuras en memoria para objetos Block y la lista; no hay almacenamiento auxiliar proporcional al número de bloques más allá de la lista misma.

## Notas prácticas / limitaciones:

- Uso de datetime.now() hace que los hashes dependan del tiempo de creación; no es determinista entre ejecuciones si se prueba con los mismos datos.
- El esquema detecta modificaciones simples (si se altera un bloque, los hashes posteriores dejan de coincidir) pero no incluye medidas de consenso, validación distribuidas ni protección contra re-cálculo de hashes si un adversario rehace bloques.
- Para producción sería necesario añadir control de integridad más robusto (firmas, proof-of-work/stake, verificación distribuida).
