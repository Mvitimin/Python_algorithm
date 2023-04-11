from typing import List
import random

class Solution:
	def partition(self, l, r, nums: List[int]):
		p = random.randint(l, r)
		pivot = nums[p]
		i = l
		nums[p], nums[r] = nums[r], nums[p]
		for j in range(l, r):
			if nums[j] >= pivot:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
		nums[i], nums[r] = nums[r], nums[i]
		return i
	
	def getMedian(self, l, r, k, nums: List[int]):
		index = self.partition(l, r, nums)
		if index == k:
			return nums[k]
		elif index < k:
			return self.getMedian(index + 1, r, k, nums)
		else:
			return self.getMedian(l, index - 1, k, nums)
		
		
	def wiggleSort(self, nums: List[int]) -> None:
		
		n = len(nums)
		if n <= 1: return 
		
		f = lambda x : (2 * x + 1) % (n | 1)
		median = self.getMedian(0, n - 1, int(n / 2), nums)
		i, j, k = 0, 0, n - 1
		while j <= k:
			if nums[f(j)] > median:
				nums[f(i)], nums[f(j)] = nums[f(j)], nums[f(i)]
				i += 1
				j += 1
			elif nums[f(j)] < median:
				nums[f(k)], nums[f(j)] = nums[f(j)], nums[f(k)]
				k -= 1
			else: j += 1
		#print(nums)
	
a = Solution()
nums = [1,5,1,1,6,4]
nums = [1, 5, 2, 2, 1, 4]
nums = [1,3,2,2,3,1]
nums = [1,5,1,1,6,4]
nums = [5,3,1,2,6,7,8,5,5]
a.wiggleSort(nums)





