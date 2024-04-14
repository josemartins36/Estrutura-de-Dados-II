# TAREFA U1T3 - Estruturas de Dados II
Esse repositório contém 2 notebooks jupyter referentes à terceira tarefa da unidade 1 de Estruturas de Dados II.

Autor: José Martins Neto

## Challenge 01: Find Closest Value.
Nessa primeira tarefa, implementou-se uma função para identificar o elemento mais próximo de um valor arbitrário, dentro de uma árvore BST. 

A função tem como argumentos a árvore e o valor target a ser procurado nela, e retorna o valor mais próximo. 

Pontua-se que o método de resolução sequencial é percorrer a árvore inteira comparando os valores encontrados com o target pela diferença absoluta — ou seja, em módulo — e armazenar o valor com menor diferença absoluta na variável a ser retornada pela função.

A complexidade do algoritmo é O(log(n)) para o caso que a árvore está balanceada.

### Challenge 02: Find Kth Largest Value.

Na segunda tarefa, implementou-se uma função para encontrar o k-ésimo maior valor presente na árvore BST.

A função utilizada tem como argumentos a árvore e o valor de 'k' arbitrário, retornando o k-ésimo maior valor.

O método de resolução recursivo é percorrer a árvore BST in-ordem, com a operação de visita do método in-ordem sendo um append em uma lista, a qual ao final do algoritmo estará ordenada em ordem crescente. Por fim lê-se o k-ésimo elemento da lista começando pelo final, ou seja, o k-ésimo maior.

Pontua-se que foi utilizado uma outra função dentro da função principal, com argumentos o nó e a lista que será ordenada, permitindo fazer operações com a árvore.

A complexidade do algoritmo implementado é O(n), em função de ser necessário percorrer a árvore inteira (custo-n elementos) alocando in-ordem numa lista. Acredito que seria possível reduzir para O(k) em uma implementação sequencial no lugar de recursiva, em que busca-se elementos
