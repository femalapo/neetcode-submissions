class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stck;

        for(string s : tokens){
            char c = s[0];
            int* nums = nullptr;
            switch(c){
                case '+':
                    nums = getNums(stck);
                    stck.push(nums[0] + nums[1]);
                    break;
                case '-':
                    if(s.length() > 1) { 
                        stck.push(stoi(s));
                        break;                 
                    }
                
                    nums = getNums(stck);
                    stck.push(nums[0] - nums[1]);
                    break;
                case '*':
                    nums = getNums(stck);
                    stck.push(nums[0] * nums[1]);
                    break;
                case '/':
                    nums = getNums(stck);
                    stck.push(nums[0] / nums[1]);
                    break;
                default:
                    stck.push(stoi(s));
                    break;
            }
            
            if(nums != nullptr) { delete[] nums; }
        }

        return stck.top();
    }

    int* getNums(stack<int>& s){
        int num2 = s.top();
        s.pop();
        int num1 = s.top();
        s.pop();
        return new int[2]{num1, num2};
    }
};
