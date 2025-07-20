# Multi-threaded Merge Sort Implementation

import threading

def merge(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def threaded_merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        # Create threads for left and right halves
        left_thread = threading.Thread(target=threaded_merge_sort, args=(arr, left, mid))
        right_thread = threading.Thread(target=threaded_merge_sort, args=(arr, mid+1, right))
        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()
        merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original array:", arr)
    threaded_merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)