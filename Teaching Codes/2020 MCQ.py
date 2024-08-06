x = 1

def myfunc(p,q):
    global x
    p, q = q, p
    x = x + p

myfunc(x,3)
print(x)
    
    
    
