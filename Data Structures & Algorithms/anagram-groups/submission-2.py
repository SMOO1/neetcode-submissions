class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}
        endList = []

        for i in range(0, len(strs)):
            word = strs[i]

            counts = [0] * 26
            for character in word:
                #ascii code of character - ascii code of a, to make a as 0
                counts[ord(character) - ord('a')] +=1 
            key = tuple(counts) # make it hashable

    

            if key not in hmap:
                hmap[key] = [word]
            else:
                hmap[key].append(word) 


        
        for x in hmap.values():
            endList.append(x)

        return endList



