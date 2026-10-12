class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size(), 0);
        int numOfZeros = 0;
        int productOfNoneZeros = 1;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                productOfNoneZeros *= nums[i];
            }else{
                numOfZeros++;
            }
        }

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                if(numOfZeros - 1 > 0){
                    res[i] = 0;
                }else{
                    res[i] = productOfNoneZeros;
                }
            }
            else{
                if(numOfZeros > 0){
                    res[i] = 0;
                }else{
                    res[i] = productOfNoneZeros / nums[i];
                }
            }
        }
        return res;
    }
};
