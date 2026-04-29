class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()

        for i in range(len(nums)):
            check=target-nums[i]
            if check in seen:
                return [seen[check],i]
            else:
                seen[nums[i]]=i


        