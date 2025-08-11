import heapq

def dijkstra(graph, start):
    # graph: {节点: [(相邻节点, 权重), ...]}
    # start: 起点
    distances = {node: float('inf') for node in graph}  # 初始化所有距离为无穷大
    print(distances)
    distances[start] = 0  # 起点到自己的距离是 0
    pq = [(0, start)]  # 最小堆（优先队列），存储 (距离, 节点)

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        # print(current_distance, current_node)
        # 如果已经有更短的路径，跳过
        if current_distance > distances[current_node]:
            print(current_distance)
            continue

        # 遍历当前节点的邻居
        for neighbor, weight in graph[current_node]:
            print(neighbor, weight)
            distance = current_distance + weight

            # 如果找到更短的路径
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

if __name__ == '__main__':
    # 定义一个带权有向图
    graph = {
        'A': [('B', 5), ('C', 2)],
        'B': [('C', 1), ('D', 3)],
        'C': [('D', 7)],
        'D': [('E', 1)],
        'E': []
    }

    # 计算从 A 出发到所有节点的最短距离
    shortest_paths = dijkstra(graph, 'A')

    # 输出结果
    for node, dist in shortest_paths.items():
        print(f"从 A 到 {node} 的最短距离: {dist}")