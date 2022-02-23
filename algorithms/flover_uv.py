import networkx as nx


def built_more_nodes(G: nx.Graph, node1: int, node2: int, u: int) -> None:
    """
    функция создает u ребер и u-1 вершин, чтобы создать путь между node1, node2, изменяя исходный граф
    
    Args:
    ------
        G: nx.Graph - исходный граф содержащий node1, node2
        node1: int - начало пути
        node2: int - конец пути
        u: int - длина пути(количество ребер)
    Returns:
    ------        
        None
    Examples:
    ------
        G = nx.Graph()
        G.add_edge(0,1)
        built_more_nodes(G, 0, 1, 3)
        G.edges
    """

    nodes = list(G.nodes)  # список из вершин
    max_node = max(nodes) + 1 # следующая вершина
    cur_node = node1
    
    for i in range(u - 1):
        G.add_edge(cur_node, max_node) # связь между текущей вершиной и новой
        cur_node = max_node  # обновление текущей вершины
        max_node += 1
        
    G.add_edge(cur_node, node2)  # замыкающая связь
    
def flower_uv(u: int, v: int, n: int) -> nx.Graph:
    """
    функция создает граф состоящий из путей длинны u,v, между вершинами соединенными ребром 
    
    Args:
    ------    
        u: int длина 1 пути при замене связи
        v: int длина 2 пути при замене связи
        n: int количество шагов построения
        
    Returns:
    ------        
        nx.Graph
        
    Examples:
    -------
        G = flower_uv(1, 2, 3)
        nx.draw(G)
    """
    G = nx.Graph()
    G.add_edge(0, 1)

    for i in range(n):
        edges = list(G.edges) # ребра на данный момент
        
        for edge in edges:
            G.remove_edge(*edge) # удаляем имеющуюся связь
            built_more_nodes(G, edge[0], edge[1], u) # новый путь длины u
            built_more_nodes(G, edge[0], edge[1], v) # новый путь длины v

    return G
  
if __name__ == "__main__":
    
    G = flower_uv(1, 2, 3)
    nx.draw(G)
