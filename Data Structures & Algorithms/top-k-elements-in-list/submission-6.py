class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}

        for num in nums:
            if num in s:
                s[num] += 1
            else: 
                s[num] = 1

        freq = {}
        for key in s:
            if s[key] in freq:
                freq[s[key]].append(key)
            else: 
                freq[s[key]] = [key]
        answer = []

        while len(answer) < k:

            greatest_key = max(freq)
            greatest_nums = freq[greatest_key]

            if len(greatest_nums) > 0:
                for num in greatest_nums:
                    answer.append(num)

                    if len(answer) == k:
                        break
            freq.pop(greatest_key)
        return answer
                
            
            

