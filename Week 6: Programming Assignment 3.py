def whole(n):
    if n==0:
        return 0
    else:
        return n+whole(n-1)
