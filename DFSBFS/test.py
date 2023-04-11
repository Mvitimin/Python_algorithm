a = set()

a.add((1, 2))
if (1, 2) in a:
	print(True)
if (1, 3) in a:
	print(True)
	
a.remove((1, 2))


l = [1, 2, 3, 4]
b = l
print(id(l))
print(id(b))
print(id(sorted(b)))
b.pop()
print(l)
print(b)

b.sort(reverse=True)
print(b)
