from typing import List
class Solution:
	def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
		def getMaxDp(arr):
			m = len(arr)
			dp = [''] * (k + 1)
			for i in range(m):
				tmp = dp[:]
				for j in range(1, min(i + 2, k + 1)):
					tmp[j] = max(tmp[j], dp[j - 1] + str(arr[i]))
				dp = tmp[:]
			return dp 
		
		dp1, dp2 = getMaxDp(nums1), getMaxDp(nums2)
		ans = ''
		for p in range(k + 1):
			t1, t2 = dp1[p], dp2[k - p]
			m, n = len(t1), len(t2)
			if m + n != k: continue
			res = ''
			i = j = l = 0
			while l < k:
				if i < m and j < n:
					if t1[i:] >= t2[j:]:
						res += t1[i]; i += 1
					else: 
						res += t2[j]; j += 1
				elif i < m:
					res += t1[i]; i += 1
				else:
					res += t2[j]; j += 1
				l += 1												
			ans = max(res, ans)
		return list(map(int, list(ans)))
				
				
																				
a = Solution()
nums1 = [3,4,6,5]; nums2 = [9,1,2,5,8,3]; k = 5
nums1 = [6,7]; nums2 = [6,0,4]; k = 5
nums1 = [3,9]; nums2 = [8,9]; k = 3
nums1 = [2,5,6,4,4,0]; nums2 = [7,3,8,0,6,5,7,6,2]; k = 15
nums1 = [8,1,8,8,6]; nums2 = [4]; k = 2


print(a.maxNumber(nums1, nums2, k))
