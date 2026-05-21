class Solution:
    def maxSumSubarray(self, nums, k):

        n = len(nums)

        # First window sum
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        # Slide the window
        for i in range(k, n):

            window_sum += nums[i]      # add new element
            window_sum -= nums[i-k]    # remove old element

            max_sum = max(max_sum, window_sum)

        return max_sum