# -*- coding:utf-8 -*-
lst = ['知乎，发现更大的世界.']
print lst
for items in lst:
	print items

for i in range(2, 101):
	for j in range(2, i):
		if i % j == 0:
			break
	else:
		print i

print ' '.join(['%s' % x for x in range(2,100) if not [y for y in range(2,x/2+1) if x % y == 0]])

import