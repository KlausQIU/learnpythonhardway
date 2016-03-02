l = []
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
	    l.append(i)
print ' '.join(str(k) for k in l)


print " ".join(["%s" % x for x in range(2,100) if not [y for y in range(2,x) if x % y ==0]])


l = []
for i in range(2,101):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        l.append(i)
print ' '.join(str(k) for k in l)