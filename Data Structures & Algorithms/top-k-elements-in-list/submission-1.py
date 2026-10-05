class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        numberMap = {}
        bucketList = [[] for x in range(len(nums) + 1)]

        for i in nums:
            if i not in numberMap:
                numberMap[i] = 1
            else:
                numberMap[i] += 1

        for number, frequency in numberMap.items():
            bucketList[frequency].append(number)
        
        finalList = []
        p = 0

        
        for i in range(len(bucketList) -1, -1, -1):
            for num in bucketList[i]:

                finalList.append(num)
                p+=1
                if p == k:
                    return finalList