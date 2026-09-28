class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        re=""
        first=strs[0]
        for i in range(len(first)):   
            for j in strs[1:]:
                if i>=len(j) or j[i]!=first[i]:
                    return re
            re+=first[i]
        return re