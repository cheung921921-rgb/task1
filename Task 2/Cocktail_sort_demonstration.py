def cocktail_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass: move the largest element to the end
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        print("After forward pass:", arr)

        if not swapped:
            break

        swapped = False
        end -= 1

        # Backward pass: move the smallest element to the start
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        print("After backward pass:", arr)

        start += 1

    return arr


# Main program
numbers = []
print("Enter 5 numbers:")
for _ in range(5):
    num = int(input("Number: "))
    numbers.append(num)

print("Original list:", numbers)
sorted_list = cocktail_sort(numbers)
print("Final sorted list:", sorted_list)

