import view as graph_visualizer

class Graph:
    def __init__(self, vertices):
        """
        Inicializa o grafo.
        V: número de vértices
        graph: lista de adjacência representada como um dicionário
        """
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v, directed=False):
        """
        Adiciona uma aresta entre u e v.
        Se o grafo não for orientado, adiciona a aresta nos dois sentidos.
        """
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

    def _hamiltonian_util(self, path, visited, current_v):
        """
        Função utilitária recursiva (backtracking) para encontrar o caminho.
        """
        
        path.append(current_v)
        visited.add(current_v)
        
        if len(path) == self.V:
            return True

        for neighbor in self.graph[current_v]:
            if neighbor not in visited:
                if self._hamiltonian_util(path, visited, neighbor):
                    return True  
                
        path.pop()
        visited.remove(current_v)
        
        return False

    def find_hamiltonian_path(self):
        """
        Tenta encontrar um Caminho Hamiltoniano no grafo.
        
        Ele tenta começar a busca a partir de cada vértice,
        pois o caminho pode começar em qualquer lugar.
        """
        
        for start_node in range(self.V):
            path = []
            visited = set()
            
            if self._hamiltonian_util(path, visited, start_node):
                print(f"Caminho Hamiltoniano encontrado partindo do nó {start_node}:")
                print(path)
                return path
        
        print("Nenhum Caminho Hamiltoniano encontrado.")
        return None

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    g_dict = g.graph
    
    print("Grafo (Lista de Adjacência):")
    print(g_dict)
    print("-" * 30)

    path = g.find_hamiltonian_path()

    print("-" * 30)

    if path:
        print(f"Visualizando o grafo e destacando o caminho: {path}")
        graph_visualizer.visualize_graph(g_dict, path, "caminho_hamiltoniano.png")
    else:
        print("Visualizando o grafo (sem caminho encontrado):")
        graph_visualizer.visualize_graph(g_dict, None, "grafo_sem_caminho.png")

    print("\n" + "=" * 30)
    print("Testando Grafo 2 (Sem Caminho)")
    g2 = Graph(5)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 2)
    g2.add_edge(3, 4)

    g2_dict = g2.graph
    
    print("Grafo (Lista de Adjacência):")
    print(g2_dict)
    print("-" * 30)
    
    path2 = g2.find_hamiltonian_path()
    
    print("-" * 30)
    print("Visualizando o grafo (sem caminho encontrado):")
    graph_visualizer.visualize_graph(g2_dict, path2, "grafo_sem_caminho_2.png")