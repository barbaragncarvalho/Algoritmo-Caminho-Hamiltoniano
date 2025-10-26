# Algoritmo-Caminho-Hamiltoniano
## Sobre o projeto
Este projeto consiste na implementação do algoritmo para encontrar um Caminho Hamiltoniano em um grafo orientado ou não orientado. A abordagem utilizada é o **backtracking**. O projeto também inclui uma visualização do grafo e do caminho encontrado, utilizando as bibliotecas `networkx` e `matplotlib`.

## Como executar o projeto

### Pré-requisitos:
Ter o Python 3 instalado. Especificamente, este projeto foi desenvolvido na versão 3.10.11 do Python.

### Passos:
• Faça o download ou clone este repositório.

• Abra o terminal ou prompt de comando e navegue até a pasta onde você salvou os arquivos.

• Execute o programa com o seguinte comando:

```python main.py```

## Lógica do algoritmo
O algoritmo consiste em utilizar uma técnica de **backtracking**, que é uma abordagem de força bruta otimizada. Ela explora recursivamente todos os caminhos possíveis a partir de um nó inicial, voltando atrás (backtrack) assim que percebe que um caminho não levará a uma solução.

### Explicação linha a linha

1. Construtor que inicializa o grafo. Foi usado uma lista de adjacência, em que cada chave é um vértice e seu valor é uma lista de seus vizinhos.
   ```
   __init__(self, vertices)
   ```

3. Função que adiciona aresta entre dois vértices. Se o grafo não for direcionado, adiciona a aresta nos dois sentidos.
   ```
   add_edge(self, u, v, directed=False)
   ```

4. Função recursiva, utilizando backtracking para encontrar o caminho.
   ```
   _hamiltonian_util(self, path, visited, current_v)
   ```

5. Nela, o vértice atual (`current_v`) é adicionado ao `path` e ao conjunto `visited`.
   ```
   path.append(current_v)
    visited.add(current_v)
   ```

6. O algoritmo verifica se o tamanho do `path` é igual ao número total de vértices (`self.V`). Se for, todos os vértices foram visitados, e um caminho Hamiltoniano foi encontrado. A função retorna `True`. Este é o caso base.
   ```
   if len(path) == self.V:
     return True
   ```

7. O algoritmo itera por todos os vizinhos (`neighbor`) do `current_v`. Se o `neighbor` ainda não foi visitado, o algoritmo faz uma chamada recursiva para si mesmo (`_hamiltonian_util(...)`), passando o `neighbor` como o novo `current_v`. Se essa chamada recursiva retornar `True`, significa que a partir daquele vizinho foi possível completar o caminho. O `True` é retornado de volta.
   ```
   for neighbor in self.graph[current_v]:
            if neighbor not in visited:
                if self._hamiltonian_util(path, visited, neighbor):
                    return True
   ```
   
8. Se o loop terminar sem que nenhum vizinho leve a uma solução (ou seja, todas as chamadas recursivas retornaram false), o algoritmo desfaz sua escolha: remove `current_v` do `path` (`path.pop()`) e do `visited` (`visited.remove(current_v)`). A função retorna `False`, sinalizando para a chamada anterior que este caminho não funcionou.
    ```
     path.pop()
     visited.remove(current_v)

     return False
    ```

9. Função que inicia a busca, tentando encontrar um Caminho Hamiltoniano no grafo. Ele tenta começar a busca a partir de cada vértice, pois o caminho pode começar em qualquer lugar.
    ```
    find_hamiltonian_path(self)
    ```

10. Itera por todos os vértices e tenta iniciar a busca a partir de cada um. Ela inicializa um `path` (lista) vazio e um `visited` (conjunto) para rastrear os nós já visitados na tentativa atual. Também chama a função auxiliar recursiva `_hamiltonian_util`. Se essa função retornar true, significa que um caminho foi encontrado, e ele é retornado.
    ```
    for start_node in range(self.V):
            path = []
            visited = set()
            
            if self._hamiltonian_util(path, visited, start_node):
                print(f"Caminho Hamiltoniano encontrado partindo do nó {start_node}:")
                print(path)
                return path
    ```

11. Se o loop terminar sem encontrar um caminho, ele informa e retorna `None`.
    ```
    print("Nenhum Caminho Hamiltoniano encontrado.")
        return None
    ```
