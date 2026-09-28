class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        a=abs(x)
        while a!=0:
            total =a%10
            rev=rev*10+total
            a//=10
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        if x>0:
            return rev
            
        
     
        
        else:
            return -rev
    
        
        return rev
        