# Write python program to store first year percentage of students in array, 
# Write functions for sorting array of floting point numbers in ascending order using quick sort and display top five scores


def partition(arr,low,high):
    
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i<=j:
            if(arr[i]<=pivot):
                i += 1
            else:
                break
        
        while i<=j:
            if(arr[i]>pivot):
                j -= 1
            else:
                break
            
        if(i<=j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        else:
            break

    temp = arr[low]
    arr[low] = arr[j]
    arr[j] = temp
    return j

def QuickSort(arr,low,high):
    if low<=high:
        pivot = partition(arr,low,high)
        QuickSort(arr,low,pivot-1)
        QuickSort(arr,pivot+1,high)

# Driver Code

n = int(input('Enter the total number of students : '))
array = []

for i in range(n):
    print('Enter the Percentage of student ',i+1,' : ')
    array.append(float(input()))

print('The unsorted array is : ',array)
QuickSort(array, 0, n - 1)
print('The Sorted Array:', array)
