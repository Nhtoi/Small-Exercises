def QuickSort(arr):
    qs(arr, 0, len(arr) - 1)

def partition(arr, low, high):
    pivot = arr[high]
    idx = low - 1
    for i in range(low, high):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]
    idx += 1
    arr[high], arr[idx] = arr[idx], pivot

    return idx

def qs(arr, low, high):
    if low >= high:
        return
    pivotIdx = partition(arr, low, high)

    qs(arr, low, pivotIdx - 1)
    qs(arr, pivotIdx + 1, high)

arr1 = [5,123,7,23,12,34,7,23,2]
QuickSort(arr1)
print(arr1)

arr2 = [12,3,6,78,2353,5,31,25]
QuickSort(arr2)
print(arr2)
