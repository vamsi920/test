
def mergeSort(ar):
    if(len(ar)>1):
        left_ar = ar[:len(ar)//2]
        right_ar = ar[len(ar)//2:]

        mergeSort(left_ar)
        mergeSort(right_ar)

        i, j, k = 0,0, 0
        while(i<len(left_ar) and j < len(right_ar)):
            if((left_ar[i]<right_ar[j])):
                ar[k] = left_ar[i]
                i+=1
            else:
                ar[k] = right_ar[j]
                j+=1
            k+=1
        while(i<len(left_ar)):
            ar[k] = left_ar[i]
            i+=1
            k+=1
        while(j<len(right_ar)):
            ar[k] = right_ar[j]
            j+=1
            k==1
    return ar
def countingSort(ar):
    a = [0]*10
    
    for i in ar:
        if(i not in a):
            a[i] = 1
        else:
            a[i]+=1
    for i in range(1,len(a)):
        a[i] += a[i-1]
    print(a)
    res = [0]*a[-1]
    for i in range(len(ar)):
        pos = a[ar[i]]-1
        res[pos] = ar[i]
        a[ar[i]]-=1
    return(res)
    
            
        
    





cArray = [1,4,1,2,7,5,2,3,3,4,7,9,2,4,6,2,7,2,7,4,3,0,4,1,5,8,9,9,3,1,4,6, 0]
print(len(cArray))
ar = [15,1,321,10,802, 2, 123, 90, 109, 11]
# print(mergeSort(ar))
countingSort(cArray)
print(len(countingSort(cArray)))

