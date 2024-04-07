import math

PREC = 10**(-6)
PI = 3.1415926535
PI_2 = 6.28318530718

def comb(n, k):
    res = 1
    if k <= n:
        for t in range(1, min(k, n - k) + 1):
            res *= n
            res /= t
            n -= 1
    else:
        res = 0
    return res

def factorial(x):
    res = 1
    for i in range(1, x+1):
        res*=i
    return res

def gcd2(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd2(a%b, b)

def gcd(*args):
    n = len(args)
    res = args[0]
    for i in range(n):
        res = gcd2(res, args[i])
    return res

def lcm2(a, b):
    return a*b//gcd2(a, b)


def lcm(*args):
    n = len(args)
    res = args[0]
    for item in args:
        res = lcm2(res, item)
    return res

def shift2Pi(x):
    sh = abs(x)//PI_2
    if x > 0:
        x -= sh*PI_2
    else:
        x += sh*PI_2
    return x

def e(x):
    prev = 0
    res = 1
    n = 1
    while abs(res-prev) > PREC:
        # print(res)
        tmp = 1
        for i in range(1,n+1):
            tmp*=x/i
        n +=1
        prev = res
        res += tmp
    return res

def sin(x):
    x = shift2Pi(x)
    prev = x - 1
    res = x
    n = 3
    flag = -1
    while abs(res-prev) > PREC:
        tmp = 1
        for i in range(1, n+1):
            tmp*=x/i
        n += 2
        prev = res
        res += tmp*flag
        flag*=-1
    return res

def cos(x):
    x = shift2Pi(x)
    prev = 0
    res = 1
    n = 2
    flag = -1
    while abs(res-prev) > PREC:
        tmp = 1
        for i in range(1, n+1):
            tmp*=x/i
        n += 2
        prev = res
        res += tmp*flag
        flag*=-1
    return res

def tan(x):
    pass
    




# print(e(5))

# print(sin(-94))

# print(cos(-150))

k = 35
n = 88
# print(factorial(n))
# print(math.factorial(n))


print(math.gcd(20, 110, 8))
print(gcd(20, 110, 8))

print(math.lcm(3, 7, 18))
print(lcm(3, 7, 18))