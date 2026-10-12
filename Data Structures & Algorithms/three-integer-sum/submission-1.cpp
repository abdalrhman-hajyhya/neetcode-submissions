class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> res;
        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++){
            int left = i + 1, right = nums.size() - 1;

            while (left < right){
                if(nums[i] + nums[left] + nums[right] == 0){
                   res.insert({nums[i], nums[left], nums[right]});
                   right--;
                }else if(nums[i] + nums[left] + nums[right] > 0){
                    right--;
                }else{
                    left++;
                }
            }
        }

        return vector<vector<int>>(res.begin(), res.end());
    }
};
