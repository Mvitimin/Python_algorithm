from typing import List
class Solution:
	def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
		dp1 = dp2 = 0
		m, n = len(nums1), len(nums2)
		i = j = 0
		
		while i < m or j < n:
			if i < m and j < n:
				if nums1[i] < nums2[j]:
					dp1 = dp1 + nums1[i]
					i += 1
				elif nums1[i] == nums2[j]:
					val = max(dp1 + nums1[i], dp2 + nums2[j])
					dp1 = dp2 = val
					i += 1; j += 1
				else:
					dp2 = dp2 + nums2[j]
					j += 1
			elif i < m:
				dp1 = dp1 + nums1[i]
				i += 1
			else:
				dp2 = dp2 + nums2[j]
				j += 1
		
		return max(dp1, dp2) % (10 ** 9 + 7)
					
															
a = Solution()
nums1 = [2,4,6,8,10]; nums2 = [4,6,8,9]
nums1 = [1,3,5,7,9]; nums2 = [3,5,100]
nums1 = [1,2,3,4,5]; nums2 = [6,7,8,9,10]
print(a.maxSum(nums1, nums2))
					
'''
event = []
		m, n = len(nums1), len(num2)
		nums = [nums1, nums2]
		dp = [[0] * (m + 1), [0] * (n + 1)]
		index = [{}, {}]
		for i in range(m):
			index[0][nums[i]] = i
			dp[0][i] += (dp[0][i - 1] + nums[i])
			event.append((nums1[i], 0, i))
		for i in range(n):
			index[1][nums[i]] = i	
			dp[1][i] += (dp[1][i - 1] + nums[i])
			event.append((nums2[i], 1, i))
		event.sort()
		for k, order, i in event:
			dp[order][i] = max(dp[order][i], dp[order][i - 1] + k)
			if k in index[order ^ 1]:
				dp[order][i] = max(dp[order][i], dp[order ^ 1][index[order ^ 1][k]])
		print(dp)
'''		
