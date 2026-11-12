def fusion(L1,L2):
    i,j,k = 0,0,0
    n = len(L1)+len(L2)
    L=[0]*n
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L[k]=L1[i]
            i=i+1
        else:
            L[k]=L2[j]
            j=j+1
        k=k+1
    
    while i <len(L1):
        L[k]= L1[i]
        i=i+1
        k=k+1
    
    while j <len(L2):
        L[k]= L2[j]
        j=j+1
        k=k+1
    
    return(L)

def tri_fusion(L):
    if len(L)==1 or len(L)==0:
        return L
    L1 = L[:len(L)//2]
    L2 = L[len(L)//2:]
    return fusion(tri_fusion(L1),tri_fusion(L2))


L=[3,5,1,6,7,8,4,2]
print(tri_fusion(L))
