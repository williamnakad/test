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

def tri_a_bulles(L):
    n=len(L)
    changement = True
    while changement == True:
        changement = False
        for i in range(n-1):
            if L[i]>= L[i+1]:
                L[i], L[i+1]=L[i+1], L[i]
                changement = True
    return(L)

L=[1,7,4,5,8,2,3,6]
print(tri_fusion(L))

M=[5,3,1,6,2,4,7,8]
print(tri_a_bulles(M))

