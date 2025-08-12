
def min_diff_in_window(A, k):
    B = []
    for i in range(len(A)):
        start = max(0, i - k + 1) #窗口起点
        window = A[start:i + 1]
        min_diff = float('inf')

        # 两两比较求差值
        for x in range(len(window)):
            for y in range(x + 1, len(window)):
                diff = abs(window[x] - window[y])
                min_diff = min(min_diff, diff)
        # 如果窗口内只有一个元素，差值为0
        if min_diff == float('inf'):
            min_diff = 0
        B.append(min_diff)
    return B

if __name__ == '__main__':
    # 测试
    A = [1, 2, 8, 4, 7]
    k = 3
    print(min_diff_in_window(A, k))  # [0, 1, 1, 2, 1]