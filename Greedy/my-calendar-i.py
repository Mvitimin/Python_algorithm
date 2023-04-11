class MyCalendar:
	
	def __init__(self):
		self.stack = []
		
	def book(self, start: int, end: int) -> bool:
		for x, y in self.stack:
			if not (end <= x or start >= y):
				return False				
		self.stack.append((start, end))
		self.stack.sort(key=lambda x:x[1])
		return True		

						
obj = MyCalendar()
array = [[10, 20], [5, 25], [20, 30]]
#array = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
for start, end in array:
	print(obj.book(start, end))
