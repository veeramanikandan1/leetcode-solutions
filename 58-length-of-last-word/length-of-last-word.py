class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        m=s.split()
        x= m[-1]
        count=0
        for i in x:
            count+=1
        return count