# https://leetcode.com/problems/count-complete-substrings/description/
# difficulty: hard
# topics: hash table, string, sliding window

# problem:
# You are given a string word and an integer k.
# A substring s of word is complete if:
#   Each character in s occurs exactly k times.
#   The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
# Return the number of complete substrings of word.
# A substring is a non-empty contiguous sequence of characters in a string.

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        def helper(substr, subLength, unique):
            complete = 0
            for window in range(k, k*unique+1, k):
                start, end = 0, window-1
                counts = Counter(substr[:end+1])
                matches = sum(1 for c in counts if counts[c] == k)
                while end < subLength:
                    if matches == (end-start+1) // k: complete += 1
                    if end+1 == subLength: break
                    old, new = substr[start], substr[end+1]
                    if counts[old] == k: matches -= 1
                    if counts[new] == k: matches -= 1
                    counts[old] -= 1
                    counts[new] += 1
                    if counts[old] == k: matches += 1
                    if counts[new] == k: matches += 1
                    start += 1
                    end += 1
            return complete
        ans = 0
        length = len(word)
        start, end = 0, 0
        while end < length:
            unique = 1
            seen = set(word[start])
            while end < length-1 and abs(ord(word[end])-ord(word[end+1])) <= 2:
                end += 1
                if word[end] not in seen:
                    seen.add(word[end])
                    unique += 1
            ans += helper(word[start:end+1], end-start+1, unique)
            end += 1
            start = end
        return ans
