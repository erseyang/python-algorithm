
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs_recursive(graph, start, visited=None):
    '''
    递归实现深度优先
    :return:
    '''
    if visited is None:
        visited = set() # 记录已经访问的节点
    visited.add(start)  # 标识当前节点
    print(start, end= '') #输出当前节点
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_stack(graph, start):
    visited = set()
    stack = [start] # 栈初始化
    # print(stack)
    while stack:
        vertex = stack.pop() #弹出栈顶节点
        print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end='')
            print(stack)
            # 将邻居逆序压栈，确保遍历顺序一致
            stack.extend(reversed(graph[vertex]))

if __name__ == '__main__':
    dfs_stack(graph, 'A')
