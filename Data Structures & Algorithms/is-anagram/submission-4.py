class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict=dict()
        for char in s:
            if char not in s_dict:
                s_dict[char]=1
            else:
                s_dict[char]+=1

        for char in t:
            if char in s_dict:
                s_dict[char]-=1
                if s_dict.get(char)==0:
                    del s_dict[char]
            else:
                return False
                
        if len(s_dict)==0:
            return True
        else:
            return False
            
        

        