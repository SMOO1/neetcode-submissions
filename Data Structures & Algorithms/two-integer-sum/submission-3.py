class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            if target - nums[i] in s:
                return [min(s[target - nums[i]], i), max(s[target - nums[i]], i)]

            else:
                s[nums[i]] = i
        return True
