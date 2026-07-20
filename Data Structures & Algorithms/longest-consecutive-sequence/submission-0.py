class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 in numSet:
                continue

            t = n
            while t + 1 in numSet:
                t += 1 

            output = max(output, 1 + t - n)

        return output
                
        