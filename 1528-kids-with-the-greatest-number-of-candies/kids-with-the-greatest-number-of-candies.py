class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        a=0
        arr=[]
        for i in range(len(candies)):
            if m<=candies[i]+extraCandies:
                arr.append(True)
            else:
                arr.append(False)
        return arr