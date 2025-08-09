
## 最长递增子序列
## 给定一个无序整数数组，找到其中最长严格递增子序列的长度。
##nums = [10, 9, 2, 5, 3, 7, 101, 18]
 ## 输出：4  # 最长递增子序列是 [2, 3, 7, 101]
def length_of_lis(nums):
    n = len(nums)
    dp = [1] * n  # 每个元素至少自身长度为1

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

## 最长公共子序列（Longest Common Subsequence, LCS）
##给定两个字符串 text1 和 text2，找出它们最长的 公共子序列 的长度。公共子序列指两个序列都出现的 不一定连续 的字符序列。
##
'''
text1 = "abcde"
text2 = "ace"
输出：3  # 最长公共子序列是 "ace"
'''
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]