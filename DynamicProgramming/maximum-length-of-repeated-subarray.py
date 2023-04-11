from typing import List

class Solution:
	def findLength(self, nums1: List[int], nums2: List[int]) -> int:
		m, n = len(nums1), len(nums2)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		ans = 0
		for i in range(m):
			for j in range(n):
				if nums1[i] == nums2[j]:
					dp[i][j] = dp[i - 1][j - 1] + 1
					ans = max(ans, dp[i][j])
		return ans


a = Solution()
nums1 = [1,2,3,2,1]; nums2 = [3,2,1,4,7]
nums1 = [0,0,0,0,0]; nums2 = [0,0,0,0,0]
nums1 = [1,1,3,2,1]; nums2 = [1, 2, 1]
print(a.findLength(nums1, nums2))
					

