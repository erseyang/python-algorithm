def knapsack_01(weights, values, capacity):
    """
    使用动态规划解决 0-1 背包问题。

    Args:
        weights (list): 物品的重量列表。
        values (list): 物品的价值列表。
        capacity (int): 背包的总容量。

    Returns:
        int: 能够装入背包的最大总价值。
    """
    num_items = len(weights)

    # 1. 定义动态规划数组 dp[i][j]
    # dp[i][j] 表示考虑前 i 个物品，背包容量为 j 时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    print(dp)
    # 2. 状态转移计算
    for i in range(1, num_items + 1):
        # 物品的索引是 i-1
        current_weight = weights[i - 1]
        current_value = values[i - 1]

        for j in range(1, capacity + 1):
            # 如果当前物品的重量超过背包容量 j，就不能放
            if current_weight > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # 否则，比较两种选择：放或不放
                # 选择一：不放第 i 个物品
                value_without_current = dp[i - 1][j]
                # 选择二：放第 i 个物品
                value_with_current = dp[i - 1][j - current_weight] + current_value
                # 取两种选择中的最大值
                dp[i][j] = max(value_without_current, value_with_current)

    # 3. 返回最终结果
    return dp[num_items][capacity]

def knapsack_02(weights, values, W):
    """
    0-1 背包 - 动态规划（二维表，便于恢复选择）
    :param weights: list of int, 每个物品的重量，长度 n
    :param values:  list of int, 每个物品的价值，长度 n
    :param W:       int, 背包容量
    :return: (max_value, taken)
             max_value: int, 能获得的最大价值
             taken: list of int (0/1), 表示每个物品是否被选中
    复杂度: 时间 O(nW)，空间 O(nW)
    """
    n = len(weights)
    # dp[i][c] 表示前 i 件物品，容量限制为 c 时可以得到的最大价值
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # 填表：对每个物品决定是否放入
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]
        for c in range(0, W + 1):
            # 不选第 i 件物品
            not_take = dp[i - 1][c]
            take = -1
            if wt <= c:
                # 可以考虑选第 i 件物品
                take = dp[i - 1][c - wt] + val
            dp[i][c] = max(not_take, take)

    max_value = dp[n][W]

    # 恢复被选中的物品（从后往前）
    taken = [0] * n
    c = W
    for i in range(n, 0, -1):
        # 如果 dp[i][c] != dp[i-1][c] 则说明第 i 件被选中
        if dp[i][c] != dp[i - 1][c]:
            taken[i - 1] = 1
            c -= weights[i - 1]  # 减去该物品重量，继续恢复
        # 否则 taken[i-1] 已经是 0，继续

    return max_value, taken

if __name__ == '__main__':
    # --- 示例 ---
    # 物品重量
    weights = [2, 3, 4, 5]
    # 物品价值
    values = [3, 4, 5, 6]
    # 背包容量
    capacity = 8

    # max_value = knapsack_01(weights, values, capacity)
    # print(f"物品重量: {weights}")
    # print(f"物品价值: {values}")
    # print(f"背包容量: {capacity}")
    # print(f"最大总价值: {max_value}")

    max_value, total_taken = knapsack_02(weights, values, capacity)
    print(f"物品重量: {weights}")
    print(f"物品价值: {values}")
    print(f"背包容量: {capacity}")
    print(f"最大总价值: {max_value}")
    print(f"选择的物品: {total_taken}")