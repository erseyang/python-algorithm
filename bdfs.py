from collections import deque


def bfs(graph, start):
    queue = deque([(start, 0)])  # (节点, 累计权重)
    visited = set()

    while queue:
        print(queue)
        node, total_weight = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(f"访问: {node}, 累计权重: {total_weight}")

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, total_weight + weight))
    return visited
# 测试
graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 2)],
    'C': [('D', 4)],
    'D': []
}

if __name__ == '__main__':
    print("\n=== BFS ===")
    visited = bfs(graph, 'A')
    print(visited)