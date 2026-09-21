import sys
import time

alist = [ 5, 6, 7, 8, 5, 44, 16, 59, 42]
blist = alist[:]
alist.sort()
print(alist)
clist = sorted(blist)
print(blist)
print(clist)

alist.sort(reverse=True)
clist = sorted(blist, reverse=True)
print(alist)
print(clist)
print(blist+clist)

dlist = [10, 20, 30]
print(dlist *4)

elist = []
for i in range(3):
    t = [1, 2, 3]
    elist.append(t)
print(elist)

flist = [ [-1]*3 for _ in range(3)]
print(flist)

N=4
card = [i+1 for i in range(N+1)]
print(card)