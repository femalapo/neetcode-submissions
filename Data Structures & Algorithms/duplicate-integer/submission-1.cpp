class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int n : nums){
            if(seen.count(n)){ // 0 = False, anything else = True
                return true;
            }
            seen.insert(n);
        }
        return false;
    }
};