A = [12,33,3,2,1,0,5,8]
target =10
def test(A,target):
    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]+A[j] == target:
                print(i,j,A[i],A[j])
                return True
    return 'false'

print(test(A,target))