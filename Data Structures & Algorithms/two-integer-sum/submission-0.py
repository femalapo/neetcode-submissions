class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dic = {}
        for i in range(len(nums)):
            if target - nums[i] not in index_dic:
                index_dic[nums[i]] = i
            else:
                return [index_dic[target - nums[i]], i]