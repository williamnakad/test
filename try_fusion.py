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

def tri_rapide(L):
    L1=[]
    L2=[]
    if L==[]:
        return L
    for i in range(1,len(L)):
        if L[i] >= L[0]:
            L2.append(L[i])
        else:
            L1.append(L[i])
    return(tri_rapide(L1)+[L[0]]+tri_rapide(L2))

L=[1,7,4,5,8,2,3,6]
print(tri_fusion(L))

M=[5,3,1,6,2,4,7,8]
print(tri_rapide(M))

