<!--
Problem 3: Rearrange Array Digits

Provide an explanation for your answer, clearly organizing your thoughts into
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

Primero se ordena la lista en orden descendente (algoritmo con complejidad O(n log n)) y luego se distribuyen los dígitos alternando entre los dos números para maximizar la suma total. Espacio adicional: O(n) para las listas temporales.