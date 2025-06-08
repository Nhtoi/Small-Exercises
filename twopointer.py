def twopointer(number):
    i = 1
    arr = []
    while i < number:
        arr.append(i)
        i += 1
    for i in range(len(arr) - 1):
        print(arr[i], arr[i + 1])
            

    return arr
 




print(twopointer(11))