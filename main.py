PREC = 10**(-6)
PI = 3.1415926535
PI_2 = 6.28318530718

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




print(e(5))

print(sin(-94))

print(cos(-150))


