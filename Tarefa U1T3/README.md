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

O método de resolução sequencial é percorrer a árvore BST in-ordem de forma decrescente, ou seja, no lugar de ser left-ação-right (in-ordem crescente) vai ser right-ação-left, com a operação de visita ocorrendo somente na iteração k, retornando assim o k-ésimo maior valor.

Pontua-se que foi utilizado uma outra função dentro da função principal, com argumento o nó, visto que a função principal não tinha ele.

A complexidade do algoritmo implementado é O(h + k), em que o custo-h (h é a altura da árvore) é para chegar no nó folha mais à direita, e o custo-k é a quantidade de vezes que a função vai executar após chegar nesse nó.
