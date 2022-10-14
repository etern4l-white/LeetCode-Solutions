class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> a;
        a.push_back(nums[0]);
        for(int i = 1; i<nums.size(); i++) {
            a.push_back(nums.at(i) + a.at(i-1));
        }
        return a;
    }
};





/*



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = [None]*len(nums)
        a[0] = nums[0]
        for i in range(1, len(nums)):
            a[i] = nums[i] + a[i-1]
        return a
        
*/
