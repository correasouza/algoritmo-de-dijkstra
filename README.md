# Observações

* Para maior facilidade com as bibliotecas necessárias, utilizar a ferramenta "Google Colab"!
* Caso deseje instalar as bibliotecas em sua máquina, siga o tutorial abaixo 👇🏼.
* https://youtu.be/MvUMAvmviaE?si=MRA8Psic26KqksIc
* Linhas de comando que você deve colar no terminal (após o tutorial do vídeo): pip install networkx,
  pip install numpy, pip install matplotlib.

 # Sobre o algoritmo de Dijkstra

O algoritmo de Dijkstra é um algoritmo guloso que encontra o menor caminho de um único vértice de origem para todos os outros vértices em um grafo ponderado. É um dos algoritmos mais importantes da teoria de grafos e tem diversas aplicações em áreas como logística, transporte e redes de computadores.

**Funcionamento:**

1. Comece com o vértice de origem e marque-o como "visitado".
2. Para cada vértice adjacente ao vértice de origem, calcule a distância total do vértice de origem ao vértice adjacente.
3. Escolha o vértice adjacente com a menor distância total e marque-o como "visitado".
4. Repita os passos 2 e 3 até que todos os vértices estejam "visitados".

**Vantagens:**

* Eficiente: O tempo de execução do algoritmo é O(E log V), onde E é o número de arestas e V é o número de vértices no grafo.
* Simples: O algoritmo é fácil de entender e implementar.
* Versátil: O algoritmo pode ser adaptado para resolver diferentes problemas de menor caminho.
  
**Aplicações:**

* Encontrar a rota mais rápida entre duas cidades em um mapa.
* Calcular o menor custo de envio de um pacote entre duas cidades.
* Encontrar o caminho mais eficiente para um robô navegar em um ambiente.



