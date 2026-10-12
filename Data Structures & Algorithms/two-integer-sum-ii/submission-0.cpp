class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;

        while (left < right){
            
            if(numbers[right] + numbers[left] > target){
                right--;
            }else if(numbers[right] + numbers[left] < target){
                left++;
            }else{
                return {left + 1, right + 1};
            }
        }
    }
};
