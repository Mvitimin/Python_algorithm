from typing import List

class Solution:
	def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
		
		m, n = len(mat), len(mat[0])
			
		def value(i, j):
			return mat[i][j] if 0 <= i < m and 0 <= j < n else -1
		
		for i in range(m):			
			l, r = 0, n - 1
			while l <= r:
				mid = l + (r - l) // 2
				
				left, right, bottom, up = value(i, mid - 1), value(i, mid + 1), value(i + 1, mid), value(i - 1, mid)
				peak = max([mat[i][mid], left, right, bottom, up])
				if mat[i][mid] == peak:
					return [i, mid]
				elif left >= right:
					r = mid - 1
				else:
					l = mid + 1			
		
		
							
a = Solution()
mat = [[1,4],[3,2]]
#mat = [[10,20,15],[21,30,14],[7,16,32]]
#mat = [[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]
#mat = [[48,36,35,17,48],[38,28,38,26,24],[15,9,33,32,6],[49,4,8,10,41]]
mat = [[750,9217,3626,2391,266,4273,9066,9569,9489,6842,4837,2498,3215,5405,3769,6224,9336],[4027,8181,9022,5531,4217,8006,8038,7551,2757,5771,2774,2294,8955,8001,3016,8883,963],[8585,555,1218,795,105,6757,2253,3792,1114,2475,150,3584,8286,7472,6115,991,7917],[7994,258,109,8720,9039,6740,195,275,8674,4502,8778,4698,281,8229,7055,2938,1754],[1579,8592,2440,3949,3145,8626,4136,5808,4380,6503,1295,6113,6653,7521,9257,3985,3701],[4915,1321,520,1532,6641,6214,6180,9056,7799,920,155,2808,1355,8190,7110,5428,9271],[1563,8654,698,3765,3464,9287,7791,4442,763,1219,4594,8898,9233,540,2939,5153,257],[3395,9618,2363,6526,1261,4904,2662,9240,3940,9285,6376,8857,5436,6289,2293,1285,8205],[5667,880,1601,7162,3804,1246,5581,9916,9759,6500,5348,486,4479,7382,8039,3738,5830],[9061,6151,7076,3044,9599,6228,1405,4840,4038,1205,1345,4391,2527,6226,2528,6384,5189],[5910,1746,1500,86,5051,7287,5897,4420,1675,2171,1431,3071,7062,7354,9126,9089,8396],[6686,1693,431,1469,5799,9081,1525,9781,9799,5316,6312,203,4782,6780,6354,1388,9168],[3978,9371,8538,2779,6238,2778,2275,4406,4934,4398,8080,2391,1037,2740,7122,4522,6900],[4912,7934,1261,5917,4124,4041,8124,9729,3204,7502,1753,2220,4992,111,6484,5444,6225]]
mat = [[7,2,3,1,2],[6,5,4,2,1]]
print(a.findPeakGrid(mat))
					
				
			