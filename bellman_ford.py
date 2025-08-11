# Python 实现 Bellman-Ford 算法相对简单，因为它不需要优先队列，只需进行多次循环遍历。
def bellman_ford(graph, num_nodes, start_node):
    """
    使用 Bellman-Ford 算法寻找最短路径，可处理负权边。

    Args:
        graph (list): 边的列表，每条边是 (源节点, 目标节点, 权重) 的元组。
        num_nodes (int): 图中节点的总数。
        start_node (str): 起点节点。

    Returns:
        dict: 键为节点，值为最短距离。如果存在负环，则返回 None。
    """
    # 初始化距离字典
    distances = {node: float('inf') for node in range(num_nodes)}
    distances[start_node] = 0

    # 进行 V-1 次松弛操作
    for _ in range(num_nodes - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # 进行第 V 次松弛操作以检测负环
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("图中存在负权环！")
            return None

    return distances
