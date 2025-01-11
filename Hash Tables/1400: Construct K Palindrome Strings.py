# https://leetcode.com/problems/construct-k-palindrome-strings/
# difficulty: medium
# topics: hash table, string, greedy, counting

# problems: Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        counts = Counter(s)
        odd = 0
        for c in counts:
            odd += counts[c] % 2
        return odd <= k

# time complexity: O(n)
# space complexity: O(26) -> O(1)
