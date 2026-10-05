class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hmapS= dict()
        hmapT = dict()

        for i in s:

            if i in hmapS:
                hmapS[i]+=1
            else: 
                hmapS[i]=1 
        for i in t:

            if i in hmapT:
                hmapT[i] += 1
            else: 
                hmapT[i]=1 

        if hmapS == hmapT:
            return True
        return False 

        
