<!--
Problem 5: Autocomplete with Tries

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

Se implementa un Trie para almacenar palabras carácter a carácter. Para autocompletar se localiza el nodo del prefijo y se recorren recursivamente sus descendientes para recoger sufijos completos. Tiempo para insertar/búsqueda del prefijo: O(m) con m la longitud de la palabra/prefijo. Espacio: proporcional al total de caracteres almacenados.