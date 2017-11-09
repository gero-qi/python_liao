def fab1(max):
    n,a,b=0,0,1
    while n <max:
        print(b,'**')
        a,b=b,a+b
        n=n+1

def fab2(max):
    n,a,b=0,0,1
    l=[]
    while n <max:
        l.append(b)
        a,b=b,a+b
        n=n+1
    return l

def fab3(max):
    n,a,b=0,0,1
    while n <max:
        yield b
        a,b=b,a+b
        n=n+1
# print(fab3(5))
# for n in fab3(5):
#     print(n)

def fab4(max):
    n,a,b=0,0,1
    while n <max:
        yield b
        a,b=b,a+b
        n=n+1

def g(x):
    yield from range(x, 0, -1)
    yield from range(x)
print(list(g(5)))
for g  in g(6):
    print(g,end=',')
