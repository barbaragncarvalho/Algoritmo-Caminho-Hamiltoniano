import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph_dict, path=None, filename="graph.png"):
    """
    Desenha o grafo usando NetworkX e Matplotlib.
    
    :param graph_dict: O grafo como um dicionário (lista de adjacência)
    :param path: Uma lista de nós representando o Caminho Hamiltoniano (se encontrado)
    :param filename: Nome do arquivo para salvar a imagem PNG
    """
    
    G = nx.Graph(graph_dict)
    
    pos = nx.spring_layout(G, seed=42)
    
    plt.figure(figsize=(10, 7))
    
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')
 
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    
    if path:
        path_edges = list(zip(path, path[1:]))
        
        nx.draw_networkx_edges(G, pos, 
                               edgelist=path_edges, 
                               width=3, 
                               alpha=0.8, 
                               edge_color='red')
        
        plt.title(f"Caminho Hamiltoniano Encontrado: {path}")
    else:
        plt.title("Grafo (Nenhum Caminho Hamiltoniano Encontrado)")

    plt.axis('off')
  
    try:
        plt.savefig(filename)
        print(f"Imagem do grafo salva como '{filename}'")
    except Exception as e:
        print(f"Erro ao salvar imagem: {e}")
    
    plt.close()