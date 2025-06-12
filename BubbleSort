
"""
First Try at Bubble Sort:
1. Wrong Comparison Pattern
2. Not Bubble Sort Logic
3. Redundant elif
4. Inefficient"""
# def BubbleSort(array):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i] > array[j]:
#                 print(array)
#                 temp = array[i]
#                 array[i] = array[j]
#                 array[j] = temp
#             elif array[i] < array[j]:
#                 continue
#     print(array)

# BubbleSort([5,4,1,8,5,6,7])

"""Second Try works"""
def BubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
    print(array)
BubbleSort([5,4,1,8,5,6,7])
