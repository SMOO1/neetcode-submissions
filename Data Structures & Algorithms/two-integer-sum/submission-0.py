class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = dict()
        
        for i in range(len(nums)):
            current = nums[i]
            wantedNum = target - current

            if wantedNum in hmap:
                return [hmap.get(wantedNum),i] 
            else:
                hmap[current] = i
        