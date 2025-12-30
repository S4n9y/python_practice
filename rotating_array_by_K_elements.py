a=list(map(int,input("enter the array:").split()))
n=len(a)
k= int(input("enter the rotations"))
while k >0:
    temp= a[n-1]   # last element
    for i in range(n -1 ,0,-1):
        a[i]=a[i-1]  # right shift of each index
    a[0]=temp  # [giving last place at front]
    print(a)
    k -=1
print(a)


# '''
# [7, 1, 2, 3, 4, 5, 6]
# [6, 7, 1, 2, 3, 4, 5]
# [5, 6, 7, 1, 2, 3, 4]
# [4, 5, 6, 7, 1, 2, 3]
# [4, 5, 6, 7, 1, 2, 3]    '''
