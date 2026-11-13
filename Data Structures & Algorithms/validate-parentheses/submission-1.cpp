#include <unordered_map>
#include <stack>

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> parens = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };

        stack<char> stck;

        for(char c : s){
            if(parens.contains(c)){
                if(stck.empty() || stck.top() != parens[c])
                {
                    return false;
                }
                stck.pop();
            }
            else
            {
                stck.push(c);
            }
        }

        return stck.empty();
    }
};
