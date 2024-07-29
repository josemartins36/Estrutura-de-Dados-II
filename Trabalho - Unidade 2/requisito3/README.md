# Tabela das redes escolhidas:
| Redes  | Qtd vértices | Qtd arestas | Degree assortativity coefficient | Qtd_comp_conectados | Tamanho do comp. gigante | Coef. de Clustering |
|----------|----------|----------|----------|----------|----------|----------|
| ODS_3  | 147   | 89    | 0.00017450864908496666    | 65   | 12    | 0.09548546691403834   |
| ODS_7  | 53    | 33    | -0.1508977900552487   | 21    | 9    | 0.03840970350404312    |
| ODS_11  | 17    | 14    | 0.9999999999999986    | 7    | 4   | 0.4117647058823529   |
| ODS_15 | 41    | 37   | 1.0000000000000009    | 16   | 4    | 0.5121951219512195    |

## Comentários:

### ODS 3 - Saúde e bem-estar:
Apesar de ser a rede com o maior número de vértices e arestas, o que indica uma alta colaboração nas atividades dos pesquisadores, a rede ODS 3 é fragmentada. Isso é evidenciado pelo alto número de componentes conectados e pelo coeficiente de assortatividade próximo de 0, o que sugere pouca ou nenhuma correlação entre os graus dos nós conectados. Ademais, o baixo coeficiente de clustering indica a formação de pequenos grupos de trabalho, com baixa interação entre os grupos.

### ODS 7 - Energia limpa e acessível:
Em contraste com a rede ODS 3, essa rede é menor e mais dispersa, apresentando o menor coeficiente de clustering das redes observadas.

### ODS 11 - Cidades e comunidades sustentáveis:
Com coeficiente de assortatividade extremamente próximo de 1, é uma rede com forte tendência de graus semelhantes se conectarem. Além disso, apresenta um coeficiente de clustering relativamente alto, indicando uma tendência dos pesquisadores de formarem grande grupos. É possível perceber também que nessa rede o tamanho do componente gigante é significativo em relação ao total de vértices, constituindo uma fração maior que das outras redes observadas. Em virtude de todas essas características, é de se esperar que seja uma rede com diversos grupos de pesquisadores e esses de graus próximos.

### ODS 15 - Vida terrestre:
Com características similares à rede ODS 11, no que tange à assortatividade e ao clustering, essa rede possui forte tendência de nós com graus semelhantes se conectarem e formarem clusters. Porém, o tamanho do componente gigante em relação ao total de vértices é uma fração menor do que a observada na rede ODS 11, indicando que essa rede é centralizada em pequenos subgrupos, destoando um pouco da rede ODS 11 que é constituida por um grande cluster.
