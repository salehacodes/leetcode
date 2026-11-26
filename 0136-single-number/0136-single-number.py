class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        output  = 0
        for num in nums:
            output = num ^ output
        return output
