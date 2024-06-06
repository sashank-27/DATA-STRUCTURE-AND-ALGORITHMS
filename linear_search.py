def linear_search(arr, target_no):
    for i in range(len(arr)):

        if arr[i] == target_no:
            return i
    return None
arr = [1,2,3,4,5,6,66,44,33,22,11]
target_no = 22
result = linear_search(arr,target_no)
print(f"element:{target_no} found at index:{result}")