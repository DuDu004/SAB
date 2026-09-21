def ten(x):
    return x*10

lambda x : x*10
alist = [1,2,3]
blist = list(map(lambda x : x*10, alist))
print(blist)

scores = [
    (80,100),
    (100,50),
    (70,100),
    (80,90)]

scores.sort(key=lambda x: (-x[0], -x[1]))

for i in scores:
    print(i[i])

def ss(x):
    return x[i]

scores.sort(key= lambda x:x[1])
print(scores)
    