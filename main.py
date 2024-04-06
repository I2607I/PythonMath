PREC = 10**(-6)

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


print(e(5))

print(sin(0))


