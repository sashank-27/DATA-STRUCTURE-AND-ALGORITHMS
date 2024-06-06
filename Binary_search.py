def binary_search(arr,target_no):
    left = 0
    right = len(arr)-1

    while (left <= right):
        mid = (left + right)//2

        if arr[mid] == target_no:
            return mid
        elif arr[mid] < target_no:
            left = arr[mid] + 1
        else:
            right = arr[mid] + 1

    return None
arr = [1,2,3,4,5,6,7,8,9]
target_no = 8
print(binary_search(arr,target_no))