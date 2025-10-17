## Reasoning Behind Decisions:

- Se encapsula la lógica de grupos y usuarios en la clase Group con métodos simples (add_group, add_user, get_groups, get_users, get_name) para mantener la API clara y facilitar pruebas.
- is_user_in_group usa una búsqueda en profundidad iterativa (pila) en vez de recursiva para evitar problemas de límite de recursión en jerarquías muy profundas y para controlar explícitamente la memoria temporal.
- Se comprueba user is None y se retorna False para evitar búsquedas innecesarias y posibles errores por entrada inválida.
- La búsqueda detiene la exploración en cuanto encuentra al usuario (early return), lo que suele mejorar el rendimiento en casos prácticos.

## Time Efficiency:

- Complejidad temporal aproximada: O(G + U_s), donde G es el número total de grupos visitados y U_s es el coste total de las comprobaciones de pertenencia en las listas de usuarios. Si consideramos N = número total de nodos (grupos) y asumimos checks de usuario O(1) promedio, se suele considerar O(N).
- En el peor caso (listas de usuarios largas y sin coincidencias tempranas) la comprobación "user in group.get_users()" puede agregar un factor proporcional al número de usuarios inspeccionados; por tanto el coste absoluto depende de la distribución de usuarios por grupo.
- Early exit reduce el coste medio cuando el usuario está cerca de la raíz o en grupos visitados tempranamente.

## Space Efficiency:

- Uso extra de memoria: O(H) para la pila, donde H es la altura máxima de la jerarquía de grupos (en el peor caso H ≈ G).
- Almacenamiento permanente: las listas de grupos y usuarios definidas en cada instancia de Group; la función no crea estructuras auxiliares proporcionales al tamaño del árbol más allá de la pila.
- Caso límite: jerarquía muy profunda (alto H) incrementa el tamaño de la pila, pero se evita el consumo adicional de la pila de llamadas del intérprete al usar un enfoque iterativo.
