'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    new_arr = []
    for i in range(len(nums)-k+1):
        largest = nums[i]
        for j in range(i, i+k):
            print(nums[j])
            if nums[j]> largest:
                largest = nums[j]
        print('________')
        new_arr.append(largest)
    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

    #wasn't able to do the large number will try later
