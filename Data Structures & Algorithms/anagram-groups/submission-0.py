class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for s in strs:
            sorted_strs.append(''.join(sorted(s)))

        seen_dic = {}
        for i in range(len(strs)):
            if sorted_strs[i] not in seen_dic:
                seen_dic[sorted_strs[i]] = [strs[i]]
            else:
                seen_dic[sorted_strs[i]].append(strs[i])

        output = []
        for l in seen_dic:
            output.append(seen_dic[l])
        return output
        