
def fibo(x):
    if(x==0):
        return 0
    if(x==1):
        return 1
    return fibo(x-1)+fibo(x-2)
    for i in range(0,10):
        print(fibo(i),end=" ")
      

def fact(x):
    if(x==0):
        return 1
    return x*fact(x-1)


def eveorodd(x):
    if(x%2==0):
        return "even"
    else:
        return "odd"
    

def prime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True


def palindrome(x):
    if(str(x)==str(x)[::-1]):
        return True
    else:
        return False


def sum(x,y):
    return x+y

def sumofn(x):
    s=0
    for i in range(1,x+1):
        s+=i
    return s


def merge(a,b):
    if(len(a)!=len(b)):
        return "not possible"
    c=[]
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    return c

def multiples(x):
    a=[]
    for i in range(1,11):
        a.append(x*i)
    return a
