class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> count;
        for(int i = 0; i < nums.size(); i++){
            count.insert(nums[i]);
        }

        int longest = 0;
        int max = 0;
        for(int num: nums){
            int current = num;
            while(count.find(current) != count.end()){
                longest++;
                current++;
            }
            if(longest > max){
                max = longest;
            }
            longest = 0;
        }

        return max;
    }
};
