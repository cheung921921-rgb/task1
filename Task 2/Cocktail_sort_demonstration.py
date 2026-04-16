def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True
# Summary
# Obtain the length of the input array
# confirm the end point and starting point
# Summary
    
    while swapped:
        swapped = False

        # Forward pass: move the largest element to the end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #swapping two element if element i > element i+1
                swapped = True
        print("After forward pass:", arr) # return the process
# Summary
# sort list from start to end
# Summary
        
        if not swapped:
            break

        swapped = False
        end -= 1

        # Backward pass: move the smallest element to the start
        for i in range(end - 1, start - 1, -1): # as the end of the array is sorted, so -1 here
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #swapping two element if element i > element i+1
                swapped = True
        print("After backward pass:", arr) # return the process

        start += 1

    return arr
# Summary
# sort array from end to start and fially return the fully sorted array
# Summary

# Main body
numbers = []
print("Enter 5 numbers:")
for _ in range(5):
    num = int(input("Number: "))
    numbers.append(num)
# Enter 5 number and put to an array

print("Original list:", numbers)
sorted_list = cocktail_sort(numbers)
print("Final sorted list:", sorted_list)

