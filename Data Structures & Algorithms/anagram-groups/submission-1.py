class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = {}
        endList = []

        for i in range(0, len(strs)):
            element = strs[i]

            sortedElement = "".join(sorted(element))

            if sortedElement not in hmap:
                hmap[sortedElement] = [element]

            else: 
                hmap[sortedElement].append(element)
        
        for x in hmap.values():
            endList.append(x)

        return endList



