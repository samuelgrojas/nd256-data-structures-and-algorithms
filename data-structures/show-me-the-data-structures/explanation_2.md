## Reasoning Behind Decisions:

- Se utiliza os.walk para recorrer recursivamente la jerarquía de directorios a partir de la ruta dada; es una solución simple y robusta que evita implementar manualmente la recursión sobre subdirectorios.
- Para cada entrada de fichero se usa file.endswith(suffix) para comprobar el sufijo solicitado; es eficiente y claro para coincidencias por extensión.
- Se construyen rutas completas con os.path.join(root, file) para devolver rutas portables y correctas independientemente del sistema operativo.
- El diseño devuelve una lista con las rutas encontradas y no altera el sistema de archivos; los tests del módulo cubren: estructura estándar con coincidencias, ausencia de coincidencias y directorio vacío.

## Time Efficiency:

- Complejidad: O(T * L) donde T es el número total de ficheros inspeccionados (más algún coste por directorios) y L es el coste de comparar el sufijo (longitud del sufijo / nombre). En la práctica suele considerarse O(T) respecto al número de ficheros y directorios visitados.
- Factores a considerar: el coste real depende del tamaño de la jerarquía, número de entradas y coste de acceso al sistema de ficheros (I/O). Para rutas muy grandes el tiempo estará dominado por I/O.

## Space Efficiency:

- Memoria usada: O(M) donde M es el número de ficheros que coinciden (tamaño de la lista resultante).  
- Overhead adicional: memoria temporal mínima para variables locales y las estructuras internas usadas por os.walk; no se mantiene en memoria la lista completa de ficheros del sistema, solo las entradas que os.walk devuelve por directorio.
- Casos límite: si suffix es cadena vacía el algoritmo devolverá todos los ficheros visitados (M ≈ T). Si la ruta no contiene coincidencias o está vacía, el uso adicional es constante aparte de la lista resultante.
