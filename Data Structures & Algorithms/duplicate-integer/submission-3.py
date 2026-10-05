class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashSet = set()

        for i in nums:
            size = len(hashSet)
            hashSet.add(i)
            if len(hashSet) == size:
                return True
        return False  
        

        
        