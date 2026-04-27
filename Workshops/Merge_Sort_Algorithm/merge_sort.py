def merge_sort(arr):
    #set base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    #for this condition to be true both items must have items 
    #Array with smallest items is depleted first

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Adding remaining elements after list with smallest items is depleted

    sorted_list.extend(left[i:]) 
    sorted_list.extend(right[j:]) #return from where they tracking index left off

    return sorted_list

    #numbers = [4, 10, 6, 14, 2, 1, 8, 5]