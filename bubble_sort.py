
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # 提前退出标志位
        swapped = False
        for j in range(0, n - i - 1):
            # 如果前一个数比后一个大，交换他们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            #如果一趟没有发生交换，说明已经排序好了
            if not swapped:
                break
    return arr