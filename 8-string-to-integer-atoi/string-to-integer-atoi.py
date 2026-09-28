class Solution: 
    def myAtoi(self, s: str) -> int:
        
        num=0
        a=1
        st=False
       
        for i in range(len(s)):
            if s[i]==" ":
                if st:
                    break
                continue
           
            if s[i]=="-" and not st:
                a=-1
                st=True 
                continue
            if s[i]=="+" and not st:
                a=1
                st=True 
                continue
            if s[i].isdigit():
                st=True 
                num = num * 10 + int(s[i])
                
                
        
            
            else:   
        
                break
        num=num*a
        if num < -2**31:
            return -2**31
            
            
        if num > 2**31 - 1:
            return 2**31 - 1
  
           
        return num