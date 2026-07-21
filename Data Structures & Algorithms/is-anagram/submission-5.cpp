class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) { return false; }

        unordered_map<char, int> countMapS;
        unordered_map<char, int> countMapT;
        for(int i = 0; i < s.length(); i++){
            countMapS[s[i]]++;
            countMapT[t[i]]++;
        }

        return countMapS == countMapT;
    }
};
