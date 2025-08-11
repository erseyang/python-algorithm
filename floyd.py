INF = float('inf')

# 初始图的邻接矩阵
dist = [
    [0,   5, INF, 10],
    [INF, 0,   3, INF],
    [INF, INF, 0,   1],
    [2, INF, INF, 0]
]

n = len(dist)

# Floyd 算法核心部分
for k in range(n):          # 中间点
    for i in range(n):      # 起点
        for j in range(n):  # 终点
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 输出结果
print("任意两点最短距离矩阵：")
for row in dist:
    print(row)

