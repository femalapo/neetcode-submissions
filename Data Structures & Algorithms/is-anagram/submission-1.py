class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_dic = {}
        for c in s:
            if c not in count_dic:
                count_dic[c] = 0

            count_dic[c] += 1

        for c in t:
            if c not in count_dic or count_dic[c] == 0:
                return False
            
            count_dic[c] -= 1

        return True