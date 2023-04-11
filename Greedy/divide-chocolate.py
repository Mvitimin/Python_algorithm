from typing import List

class Solution:
	def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
		if K == 0:
			return sum(sweetness)
		left, right = 0, sum(sweetness)
		while left <= right:
			mid = left + (right - left) // 2
			piece = cnt = 0
			for s in sweetness:
				piece += s
				if piece >= mid:
					cnt += 1
					piece = 0
			if cnt >= K + 1:
				left = mid + 1
			else:
				right = mid - 1
		return right

a = Solution()
sweetness = [1,2,3,4,5,6,7,8,9]; K = 5
#sweetness = [5,6,7,8,9,1,2,3,4]; K = 8
sweetness = [1,2,2,1,2,2,1,2,2]; K = 2
print(a.maximizeSweetness(sweetness, K))						

