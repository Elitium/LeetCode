import math

class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)

        dp = [[-math.inf] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = nums1[i] * nums2[j]

                dp[i][j] = max(
                    product + max(0, dp[i+1][j+1]),
                    dp[i+1][j],
                    dp[i][j+1]
                )

        return dp[0][0]
