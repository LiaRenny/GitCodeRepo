# Binary Search for DSA Algorithm

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found, return index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Not found

if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
    target = int(input("Enter number to search: "))
    index = binary_search(arr, target)
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")