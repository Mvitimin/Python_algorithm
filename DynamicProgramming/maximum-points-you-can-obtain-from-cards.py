
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
from typing import List

class Solution:
	def maxScore(self, cardPoints: List[int], k: int) -> int:
		if k == len(cardPoints):
			return sum(cardPoints)
					
		left = [0]
		right = [0]
		for i in range(k):
			left.append(left[i] + cardPoints[i])
			right.append(right[i] + cardPoints[len(cardPoints) - 1 - i])
		
		ans = 0	
		for r in range(k + 1):
			ans = max(ans, right[r] + left[k - r])
			
		return ans		
			
		
a = Solution()


#cardPoints = [1,79,80,1,1,1,200,1]
#k = 3
#cardPoints = [1,1000,1]
#k = 1
cardPoints = [1,2,3,4,5,6,1]
k = 3

print(a.maxScore(cardPoints, k))
