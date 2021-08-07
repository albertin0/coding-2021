def getnxtInd(arr,i,n):
    p = 0
    ind = i + int(pow(2,p))
    while ind<n and arr[i]==arr[ind]:
        p+=1
        ind = i + int(pow(2,p))
    if p==0:
        return i
    else:
        return i + int(pow(2,p-1))

arr = [int(i) for i in input().split(' ')]
n = int(len(arr))
sol = -1
l = 0
i = 0
while i < n:
    temp_i = i
    prev_i = -1
    while temp_i!=prev_i:
        prev_i = temp_i
        temp_i = getnxtInd(arr,prev_i,n)
    temp_l = prev_i-i+1
    if temp_l>l:
        l = temp_l
        sol = arr[i]
    i = prev_i + 1

print(sol,l)