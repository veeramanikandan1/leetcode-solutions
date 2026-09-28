class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        arr=[]
        while left<right:   
            k=min(height[left],height[right])
            s=right-left
            area=k*s
            arr.append(area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max(arr)