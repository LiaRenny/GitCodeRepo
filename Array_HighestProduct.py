# The highest product of any three numbers in an array.

def highest_product_of_three(arr):
    arr.sort()
    # Product of three largest
    prod1 = arr[-1] * arr[-2] * arr[-3]
    # Product of two smallest and the largest
    prod2 = arr[0] * arr[1] * arr[-1]
    return max(prod1, prod2)

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Original array:", arr)
    result = highest_product_of_three(arr)
    print("Highest product of any three numbers:", result)