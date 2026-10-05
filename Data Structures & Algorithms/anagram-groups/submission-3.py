class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in x:
                x[sorted_word].append(word)
            else:
                x[sorted_word] = [word]
        z = []
        for key in x:
            z.append(x[key])

        return z
        