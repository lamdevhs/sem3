def listeN(n):
    return range(n+1)

def map(f, l):
    out = []
    for i in range(len(l)):
        e = f(l[i])
        out.append(e)
    return out
    
def left(e):
    (x,_) = e
    return x
def right(e):
    (_,x) = e
    return x

def separe(xs):
    leftList = map(left, xs)
    rightList = map(right, xs)
    return (leftList,rightList)
    

def t():
    print listeN(5)
    xs = [(1,2),(3,4),(5,6)]
    print separe(xs)

t()