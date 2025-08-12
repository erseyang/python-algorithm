import math

## 使用矩阵来表示图
def dijkstra_matrix(graph, start):
    n = len(graph)
    visited = [False] * n
    dist = [math.inf] * n
    dist[start] = 0

    for _ in range(n):
        # 1. 找到当前未访问节点中距离最小的节点
        u = -1
        mid_dist = math.inf
        for i in range(n):
            if not visited[i] and dist[i] < mid_dist:
                min_dist = dist[i]
                u = i
        if u == -1: #剩余节点不可达
            break
        visited[u] = True
        # 2. 用u更新它的邻居节点
        for v in range(n):
            if not visited[v] and graph[u][v] != math.inf:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]

    return dist

if __name__ == '__main__':
    ## 1
    # 测试
    INF = math.inf
    graph = [
        [0, 2, 6, INF],
        [INF, 0, 3, 1],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    start_node = 0
    result = dijkstra_matrix(graph, start_node)
    print(f"从节点 {start_node} 出发的最短路径：", result)
