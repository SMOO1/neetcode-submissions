class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        for ch in s:
            if ch not in s1:
                s1[ch] = 1
            else:
                s1[ch]+=1
        
        for ch in t:
            if ch not in s2:
                s2[ch] = 1
            else:
                s2[ch]+=1

        if s1 == s2:
            return True
        else:
            return False
        
