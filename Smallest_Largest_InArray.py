#Smallest and Largest Elements in an Unsorted Array

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original array:", arr)
smallest = min(arr)
largest = max(arr)
print("Smallest Element: ", smallest)
print("Largest Element: ", largest)