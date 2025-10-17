# Analysis

Documentación del tiempo de ejecución (peor caso) para cada tarea.

## Task0

**Descripción**: Se leen los ficheros `texts.csv` y `calls.csv`. Se imprime el primer registro de `texts` y el último registro de `calls`.

**Enfoque**: Cargar ambos CSVs en listas y acceder por índice a `texts[0]` y `calls[-1]`.

**Análisis de complejidad**:
- **Algoritmo**: Lectura completa de ambos ficheros en listas (iterar todos los registros) + dos accesos directos por índice.
- **Notación Big-O (tiempo)**: O(n + m) donde n = número de registros en `texts`, m = número de registros en `calls`. Si se define N = n + m, entonces O(N).
- **Justificación**: La operación dominante es transformar el lector CSV en listas (recorrer cada registro una vez). Los accesos por índice son O(1).

## Task1

**Descripción**: Contar cuántos números de teléfono distintos aparecen en los registros de `texts` y `calls`.

**Enfoque**: Recorrer todos los registros de `texts` y `calls`, insertar los números en un set y devolver su tamaño.

**Análisis de complejidad**:
- **Algoritmo**: Dos bucles que recorren todos los registros y operaciones de inserción en un set.
- **Notación Big-O (tiempo)**: O(n + m) donde n = registros en `texts`, m = registros en `calls`. Con N = n + m, O(N).
- **Justificación**: Cada registro se procesa una vez; las inserciones en set son O(1) promedio (hash). Lectura de archivos incluida en el conteo.

## Task2

**Descripción**: Encontrar el número que pasó más tiempo en llamadas (sumando tanto las salientes como las entrantes).

**Enfoque**: Recorrer `calls`, acumular duración por número en un diccionario, luego obtener la clave con valor máximo.

**Análisis de complejidad**:
- **Algoritmo**: Un bucle sobre todos los registros de `calls` que hace actualizaciones O(1) en un diccionario; al final, una operación `max` que recorre todas las claves del diccionario.
- **Notación Big-O (tiempo)**: O(m + u) donde m = número de llamadas y u = número de números únicos (u ≤ 2m). En términos de m, O(m). Con M = m, O(M).
- **Justificación**: Actualizar el diccionario por cada llamada es O(1) promedio; la búsqueda del máximo requiere recorrer todas las claves (O(u)). Puesto que u está acotado por O(m), el coste total es O(m).

## Task3

**Descripción**: 
- Parte A: Encontrar todos los códigos (códigos de área y prefijos móviles) a los que llaman números de Bangalore `(080)`.
- Parte B: Calcular el porcentaje de llamadas desde `(080)` hacia otros `(080)`.

**Enfoque**: Recorrer `calls` una vez; para las llamadas iniciadas por `(080)` extraer el código del receptor según su formato y añadirlo a un set; contar totales y calcular porcentaje. Ordenar el set antes de imprimir.

**Análisis de complejidad**:
- **Algoritmo**: Un bucle sobre `calls` con operaciones de comprobación de prefijos y extracción de subcadenas (O(1) por registro), construcción de un set de códigos, y finalmente ordenación del set.
- **Notación Big-O (tiempo)**: O(m + k log k) donde m = número de llamadas y k = número de códigos únicos encontrados. En el peor caso k = O(m), por lo que O(m log m).
- **Justificación**: El recorrido de llamadas es O(m). La ordenación de los k códigos es O(k log k) y domina si k es proporcional a m. Cálculo del porcentaje y operaciones de cadena son O(1) por registro.

## Task4

**Descripción**: Identificar números que podrían ser telemarketers: números que hacen llamadas salientes pero nunca envían/reciben textos ni reciben llamadas.

**Enfoque**: Construir cuatro conjuntos: outgoing_calls, incoming_calls, text_senders, text_receivers; calcular diferencia de conjuntos y ordenar el resultado antes de imprimir.

**Análisis de complejidad**:
- **Algoritmo**: Recorrer `calls` para llenar dos sets, recorrer `texts` para llenar otros dos sets, computar diferencia de conjuntos y ordenar el conjunto resultante.
- **Notación Big-O (tiempo)**: O(m + n + p log p) donde m = llamadas, n = textos y p = número de candidatos resultantes (p ≤ número total de números únicos). En el peor caso p = O(m + n) y la complejidad es O((m + n) log(m + n)).
- **Justificación**: Construir los sets requiere una pasada por cada fichero (O(m) y O(n)). La operación de diferencia entre sets es O(u) donde u es el número de elementos involucrados (≤ m+n). Ordenar los p candidatos es O(p log p) y puede dominar si p es grande.

Notas generales:
- En todos los scripts la lectura de los CSVs (list(reader)) implica tiempo lineal respecto al número de registros; por simplicidad se ha incluido en los términos n, m, etc.
- Las operaciones con sets y diccionarios se consideran O(1) en promedio (operaciones de hash). En escenarios adversos por colisiones de hash la complejidad podría degradarse, pero no es el caso habitual.


