class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashSet = set()

        for i in nums:
            hashSet.add(i)

        if len(nums) == len(hashSet):
            return False

        return True
        