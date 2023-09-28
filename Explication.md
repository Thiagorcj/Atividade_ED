# Explicação dos códigos:

## Algoritmo BFS (Busca em Largura) para encontrar o caminho mais curto entre dois vértices em um grafo:

Primeiro, são criados vetores dist e ant, que são usados para armazenar informações sobre o caminho mais curto. dist guarda as distâncias de vertice1 para todos os outros vértices, e ant armazena os antecessores de cada vértice ao longo do caminho.

Também é criada uma lista isVisited, que atua como uma bandeira para indicar se um vértice já foi visitado durante o processo.

O vértice de partida, vertice1, tem sua distância definida como zero, uma vez que é o ponto de partida.

Em seguida, inicia-se um loop que continua até que a fila Q esteja vazia. Essa fila é usada para controlar a ordem de visitação dos vértices.

A cada iteração do loop, um vértice p é retirado da fila. Se p for igual a vertice2, o processo é interrompido, pois encontramos o caminho mais curto.

Para cada vértice adjacente a p no grafo, verificamos se ele já foi visitado. Se não foi, atualizamos a distância e o antecessor desse vértice e o colocamos na fila Q para futura análise.

Após a conclusão do loop, verificamos se a distância até vertice2 ainda é -1. Se for o caso, isso significa que não há um caminho entre os dois vértices.

Caso contrário, reconstruímos o caminho mais curto percorrendo os antecessores a partir de vertice2 até vertice1. Os vértices são empilhados em uma lista e, em seguida, desempilhados para imprimir o caminho na ordem correta

## Algoritmo de busca em profundidade(usando pilha):

Primeiramente, criamos uma bandeira para rastrear se os elementos estão presentes ou não na pilha. Além disso, inicializamos uma lista que irá armazenar os elementos do grafo e criamos uma lista chamada "pilha" que funcionará de maneira semelhante a uma estrutura de pilha.

O processo começa adicionando o vértice inicial como um parâmetro à pilha. Enquanto a pilha não estiver vazia, o seguinte procedimento é executado:

Um vértice, é retirado da pilha usando a operação pop e v recebe o retorno dessa operação, ou seja, o próprio vetor que foi retirado.
Verificamos se v já foi visitado. Se não tiver sido visitado, adicionamos v à lista de elementos que será impressa posteriormente e v passa a ter o “status” de  visitado.
Para cada vizinho de v que ainda não foi visitado, adicionamos esse vizinho à pilha. Isso garante que todos os elementos sejam visitados e adicionados à lista de elementos que será impressa ao final do processo.


