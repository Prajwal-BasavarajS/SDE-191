
class Solution:
    def maxSubArrayBruteForce(self, nums):
        n = len(nums)
        max_sum = float('-inf')
        
        # Check all subarrays
        for i in range(n):
            for j in range(i, n):
                current_sum = sum(nums[i:j+1])  # sum of subarray nums[i...j]
                max_sum = max(max_sum, current_sum)
        
        return max_sum
    
s = Solution()

nums = [2, 3, 5, -2, 7, -4]

print("Brute Force:", s.maxSubArrayBruteForce(nums))


def max_subarray_bruteforce(nums):
    n = len(nums)
    max_sum = float('-inf')
    
    # Check all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(nums[i:j+1])  # sum of subarray nums[i...j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_better(nums):
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    
    return max_sum


class Solution:
    def maxSubArrayBetterBruteForce(self, nums):
        n = len(nums)
        max_sum = float('-inf')

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        
        return max_sum




class Solution:
    def maxSubArrayKadane(self, nums):
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum



s = Solution()
nums = [2, 3, 5, -2, 7, -4]

print("Brute Force:", s.maxSubArrayBruteForce(nums))
print("Better Brute Force:", s.maxSubArrayBetterBruteForce(nums))
print("Prefix Sum:", s.maxSubArrayPrefix(nums))
print("Kadane’s Algorithm:", s.maxSubArrayKadane(nums))

