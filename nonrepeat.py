
def non_repeat(arr, n):
    for i in range(0, n):
        count = 0
        for j in range(0,n):
            if arr[i] == arr[j]:
                count = count+1
        if count == 1:
            print(arr[i])

non_repeat([3,4,5,6,6,4], 6)
