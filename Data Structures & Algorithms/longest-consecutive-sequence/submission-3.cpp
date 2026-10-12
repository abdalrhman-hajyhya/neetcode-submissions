class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> count;
        for(int i = 0; i < nums.size(); i++){
            count.insert(nums[i]);
        }
        int longest = 0;
        for(int num : nums){
            
            if(count.find(num - 1) == count.end()){
                int lenght = 0;
                int current = num;
                while(count.find(current) != count.end()){
                    lenght++;
                    current++;
                }
                longest = max(longest , lenght);
            }   
            
        }
        return longest;
    }
};
