def max_sum_subarray(nums, k):
	"""Return the largest sum among all contiguous subarrays of length k."""
	if not 1 <= k <= len(nums):
		raise ValueError("k must be between 1 and len(nums)")

	window_sum = sum(nums[:k])
	largest_sum = window_sum

	for right in range(k, len(nums)):
		window_sum += nums[right] - nums[right - k]
		largest_sum = max(largest_sum, window_sum)

	return largest_sum


def longest_unique_substring_length(text):
	"""Return the length of the longest substring without repeated characters."""
	last_seen = {}
	left = longest = 0

	for right, char in enumerate(text):
		if char in last_seen:
			left = max(left, last_seen[char] + 1)
		last_seen[char] = right
		longest = max(longest, right - left + 1)

	return longest


if __name__ == "__main__":
	nums = [2, 1, 5, 1, 3, 2]
	k = 3
	result = max_sum_subarray(nums, k)
	print(f"Input: nums={nums}, k={k}")
	print(f"Output: {result}")
