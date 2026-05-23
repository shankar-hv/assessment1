#second Largest in the array

array = [3, 1, 4, 1, 5, 9, 2, 6]

def secondLargest(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    return arr[i]
print(secondLargest(array))