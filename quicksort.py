list = [54, 46, 33, 52, 31]

def q_s(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return q_s(left) + [pivot] + q_s(right)
print(q_s(list))