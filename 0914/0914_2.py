def nmax(x,y):
    if x > y:
        return x
    return y

a =10
b= 20
print(nmax(a,b))

def ten(x):
    return x*10

lambda x : x*10
alist = [1,2,3]
blist = list(map(lambda x : x*10, alist))
print(blist)