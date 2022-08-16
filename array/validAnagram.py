# https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Runtime: 50 ms beats 91.80%
        Memory Usage: 14.5 MB beats 35.25%
        """
        # string not equal length
        if len(s) != len(t):
            return False

        count = dict()
        # count all characters in s
        for i in s:
            count[i] = 1 + count.get(i, 0)

        for i in t:
            # if character not in count dict, return False
            if i not in count:
                return False
            else:
                count[i] -= 1

        return all(v == 0 for v in count.values())
