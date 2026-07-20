class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dic = {}
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            frequency_dic[n] = 1 + frequency_dic.get(n, 0)
        
        for n, f in frequency_dic.items():
            buckets[f].append(n)

        output = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                output.append(n)
                if len(output) == k:
                    return output