class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=dict()
        for num in nums:
            if num in seen and seen.get(num,0)==1:
                return True
            seen[num]=1
        return False
            
        