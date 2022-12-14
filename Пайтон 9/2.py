def ab():
    a = list(map(int, input().split()))
    k = len(a)
    n = abs(a[0])
    max = 0
    
    for i in range(1, k):
        min = abs(a[i])
        if min > n:
            min = n
    
    for i in range(1, k):
        if a[i] >= 0:
            pass
        elif a[i] < a[i-1]:
            max = a[i]

    return min, max    
        
print(ab())