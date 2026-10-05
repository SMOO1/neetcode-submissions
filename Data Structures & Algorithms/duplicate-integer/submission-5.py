class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letters = {}

        for i in nums:
            if i in letters:
                return True

            else:
                letters[i] = 1

        return False


        
        