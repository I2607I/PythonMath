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

print(e(5))


