with open("rosalind_mer", "r", encoding="utf-8") as file: 
    n = int(file.readline().strip())
    A = list(map(int, file.readline().strip().split()))
    m = int(file.readline().strip())         
    B = list(map(int, file.readline().strip().split()))
    c = []
    i = 0
    j = 0
    while i<n and j<m: 
        if A[i] <= B[j]: 
            c.append(A[i])
            i+=1
        else: 
            c.append(B[j])
            j+=1
    while i<n: 
        c.append(A[i])
        i+=1
    while j<m: 
        c.append(B[j])
        j+=1
print(' '.join(map(str,c)))