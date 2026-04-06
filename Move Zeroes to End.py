'''
Move Zeros to End (Array)
Problem

Move all 0s to the end while maintaining order of other elements.

Example
Input:
[4, 5, 0, 1, 9, 0]

Output:
[4, 5, 1, 9, 0, 0]

'''

arr = [4, 5, 0, 1, 9, 0]

count = 0 
for i in range(len(arr)):
    if arr[i] != 0:
        arr[count] = arr[i]
        count += 1
for i in range(count, len(arr)):
    arr[i] = 0
print(arr)