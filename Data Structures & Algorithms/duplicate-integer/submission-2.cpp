#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> seen;
        for(int& num: nums){
            if(seen.count(num) == 0){
                seen[num] = 1;
            }else{
                return true;
            }
        }
        return false;
    }
};
