# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(p):
    i=0
    j=0
    l=len(p)
    if l==0:return True
    
    #while i< l:
    #    if p[i][i]!=0:
    #        return False
        i=i+1
    i=0
    
    r=len(p[0])
    
    if r==l:
        while i<l:
            
            j=i
            while j<l:
                if p[i][j]!=-p[j][i]:
                    return False
                j=j+1
            i=i+1
        return True
    else:
        return False

# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, -2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False
