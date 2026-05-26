def min_subarray_len(target, arr):

    # Left pointer of window
    left = 0

    # Stores current window sum
    current_sum = 0

    # Stores minimum length found
    # Initially infinite because we haven't found any valid subarray yet
    min_length = float('inf')


    # Right pointer expands the window
    for right in range(len(arr)):

        # Add current element into window sum
        current_sum += arr[right]

        print("\nWindow Expanded")
        print("Added:", arr[right])
        print("Current Window:", arr[left:right+1])
        print("Current Sum:", current_sum)


        # If window sum becomes >= target
        # then try shrinking from left side
        while current_sum >= target:

            print("\nCondition Met (sum >= target)")
            print("Current Valid Window:", arr[left:right+1])

            # Calculate current window length
            window_length = right - left + 1

            # Store smallest length
            min_length = min(min_length, window_length)

            print("Window Length:", window_length)
            print("Minimum Length So Far:", min_length)


            # Remove left element from sum
            print("\nShrinking Window")
            print("Removing:", arr[left])

            current_sum -= arr[left]

            # Move left pointer forward
            left += 1

            print("New Window:", arr[left:right+1])
            print("New Sum:", current_sum)


    # If no valid subarray found
    if min_length == float('inf'):
        return 0

    return min_length



# Input array
arr = [2,3,1,2,4,3]

# Target sum
target = 7

# Function call
answer = min_subarray_len(target, arr)

print("\nFinal Answer:", answer)