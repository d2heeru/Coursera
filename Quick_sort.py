def swap (a,b):
    temp=a
    a=b
    b=temp

def partition(a,low,high):
    pivot=a[high]
    i=low-1
    for j in range(low,high-1):
        if a[j] <= pivot:
            i=i+1
            swap(a[i],a[j])
    swap(a[i+1],a[high])
    return i+1
def quick_sort(a,low,high):
    if low < high:
        s=partition(a,low,high)
        quick_sort(a,low,s-1)
        quick_sort(a,s+1,high)

a=[10,7,8,9,1,5]
quick_sort(a,0,len(a)-1)
