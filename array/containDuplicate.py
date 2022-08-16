# https://leetcode.com/problems/contains-duplicate/submissions/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        using set
        Runtime: 764 ms, faster than 35.72% 
        Memory Usage: 26 MB, less than 71.55% 
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    def containDuplicate2(self, nums: List[int]) -> bool:
        """
        using dictionary
        Runtime: 646 ms, faster than 58.03% 
        Memory Usage: 26 MB, less than 30.33%
        """
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True
        return False
