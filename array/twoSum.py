# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 114 ms beats 50.41%
        Memory Usage: 15.1 MB beats 50.22%
        """
        seen = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in seen:
                return [seen[diff], value]
            seen[value] = index
