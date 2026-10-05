class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(0, len(nums)):
            goal = target - nums[i]


            if goal in s:
                return [s[goal], i] 
            else:
                s[nums[i]] = i