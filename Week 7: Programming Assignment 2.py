def Transpose(M):
    n = len(M)
    m = len(M[0])
    for i in range(0,n):
        for j in range(i+1,m):
            temp = M[i][j]
            M[i][j] = M[j][i]
            M[j][i] = temp
            
    return M
