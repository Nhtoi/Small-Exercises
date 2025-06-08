import math

#before watching video, works but not truly B.S O(n log n) 
#does not retrieve index of the number in the array

def FirstAttempt(array, target):
    newarray = []
    subArr1 = []
    subArr2 = []

    half = math.floor(len(array) / 2)  
    subArr1 = array[:half]
    subArr2 = array[half:]
    if not subArr1 or not subArr2:
        return print("Target not in Array")
    # print(subArr1,subArr2 )
    if subArr1[-1] < target:
        newarray = subArr2
    if subArr1[-1] > target:
        newarray = subArr1 
    if subArr1[-1] == target or subArr2[-1] == target:
        return print("Target found")
   
    return FirstAttempt(newarray, target)

# FirstAttempt([1, 2, 4, 5, 6, 7], 3)
# FirstAttempt([1, 2], 2)
# FirstAttempt([1, 2, 4, 5, 6, 7], 11)
# FirstAttempt([1, 3, 5, 7, 9, 11], 5)
# FirstAttempt([1, 2, 3, 4, 5, 6], 4)
# FirstAttempt([1, 2, 3, 4, 5, 6, 7, 8], 6)
# FirstAttempt([1, 3, 5, 7, 9], 4)
# FirstAttempt([1, 3, 4, 6, 8, 10], 1)
# FirstAttempt([3], 5)
# FirstAttempt([1, 3], 2)
# FirstAttempt([1, 2, 3], 10)
# FirstAttempt([1, 3, 5, 7, 9, 11, 13], 6)
# FirstAttempt([1, 2], 1)

#After Watching Video its faster O(logn) but logic is still flawed 
#however it finds the index in the array where the number is found

def SecondAttempt(array, target):
    if target == array[0]:
        return print("Found target:", target,"at Index:", 0)
    if target == array[-1]:
        return print("Found target:", target,"at Index:", len(array) - 1)
    i = 0
    j = len(array) - 1
    middle = (i+j) // 2
    # print(middle)
    while i != j:
        if target < array[middle]:
            j = middle - 1
            middle = (i+j) // 2
        if target > array[middle]:
            i = middle + 1
            middle = (i+j) // 2 
        if array[i] == target:
            return print("Found target:",target,"at Index:", abs(i)) 
        if array[j] == target:
            return print("Found target:",target,"at Index:", abs(j))
        if array[middle] == target:
            return print("Found target:", target,"at Index:", middle)
    return print("target:",target, "Not Found in array")
        
# SecondAttempt([1, 2, 4, 5, 6, 7], 3) #not in array
# SecondAttempt([1, 2], 2) #in array
# SecondAttempt([1, 2, 4, 5, 6, 7], 11) #not in array
# SecondAttempt([1, 3, 5, 7, 9, 11], 5) #in array 
# SecondAttempt([1, 2, 3, 4, 5, 6], 4) #in array
# SecondAttempt([1, 2, 3, 4, 5, 6, 7, 8], 6) #in array
# SecondAttempt([1, 3, 5, 7, 9], 4) #not in array
# SecondAttempt([1, 3, 4, 6, 8, 10], 10) #in array 
# SecondAttempt([3], 5)
# SecondAttempt([1, 3], 2)
# SecondAttempt([1, 2, 3], 10)
# SecondAttempt([1, 3, 5, 7, 9, 11, 13], 6)
# SecondAttempt([1, 2], 1)

#Another attempt this time fully watching the video

def ThirdAttempt(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return print("Found Target:", target, "At index", mid)
        elif array[mid] > target:
            right = mid - 1 
        elif array[mid] < target:
            left = mid + 1  
    return print(-1)

# ThirdAttempt([1, 2, 4, 5, 6, 7], 3) #not in array
# ThirdAttempt([1, 2], 2) #in array
# ThirdAttempt([1, 2, 4, 5, 6, 7], 11) #not in array
# ThirdAttempt([1, 3, 5, 7, 9, 11], 5) #in array 
# ThirdAttempt([1, 2, 3, 4, 5, 6], 4) #in array
# ThirdAttempt([1, 2, 3, 4, 5, 6, 7, 8], 6) #in array
# ThirdAttempt([1, 3, 5, 7, 9], 4) #not in array
# ThirdAttempt([1, 3, 4, 6, 8, 10], 10) #in array 
# ThirdAttempt([3], 5) #not in array
# ThirdAttempt([1, 3], 2) #not in array
# ThirdAttempt([1, 2, 3], 10) #not in array
# ThirdAttempt([1, 3, 5, 7, 9, 11, 13], 6) #not in array
# ThirdAttempt([1, 2], 1) #in array
