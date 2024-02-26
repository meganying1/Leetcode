# https://leetcode.com/problems/longest-duplicate-substring/description/
# difficulty: hard
# topics: string, binary search, sliding window, rolling hash, suffix array, hash function

# problem:
# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
# Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

mod = (10**9) + 7
mods = []
curr = 1
for i in range(3 * 10**4):
    mods.append(curr)
    curr *= 26
    curr %= mod

class Solution:

    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        lo, hi = 1, length-1
        ans = ""

        def getVal(c):
            return ord(c)-ord('a')+1

        def returnDup(size):
            seen = {}
            start, end = 0, size-1
            hashVal = 0
            hashCoords = defaultdict(list)
            for i in range(size): hashVal = (hashVal * 26 + getVal(s[i])) % mod
            while end < length+1:
                if hashVal in hashCoords: 
                    newStr = s[start:end+1]
                    for (prevStart, prevEnd) in hashCoords[hashVal]:
                        if s[prevStart:prevEnd] == newStr: return newStr
                hashCoords[hashVal].append((start, end+1))
                if end+1 == length: break
                hashVal -= (getVal(s[start]) * mods[size-1]) % mod
                hashVal *= 26
                hashVal += getVal(s[end+1])
                hashVal %= mod
                start += 1
                end += 1
            return ""

        while lo <= hi:
            size = lo + ((hi-lo)//2)
            dup = returnDup(size)
            if dup != "":
                ans = dup
                lo = size+1
            else: hi = size-1
        return ans

"""
mod = (10**9) + 7
mods = []
curr = 1
for i in range(3 * 10**4):
    mods.append(curr)
    curr *= 10
    curr %= mod

class Solution:

    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        lo, hi = 1, length-1
        ans = ""

        def getVal(c):
            return ord(c)-ord('a')+1

        def returnDup(size):
            seen = {}
            start, end = 0, size-1
            hashVal = 0
            hashMap = defaultdict(set)
            for i in range(size): hashVal = (hashVal * 10 + getVal(s[i])) % mod
            while end < length+1:
                if hashVal in hashMap: 
                    newStr = s[start:end+1]
                    for (prevStart, prevEnd) in hashMap[hashVal]:
                        if s[prevStart:prevEnd] == newStr: return newStr
                hashMap[hashVal].add((start, end+1))
                if end+1 == length: break
                hashVal -= (getVal(s[start]) * mods[size-1]) % mod
                hashVal *= 10
                hashVal += getVal(s[end+1])
                hashVal %= mod
                start += 1
                end += 1
            return ""

        while lo <= hi:
            size = lo + ((hi-lo)//2)
            dup = returnDup(size)
            if dup != "":
                ans = dup
                lo = size+1
            else: hi = size-1
        return ans
"""
# hashMap name can get kind of confusing, bad variable naming practice in SWE
# no reason to make it a defaultdict(set), aren't leverating set in any way; list is less expensive if you aren't using benefits of a set
# do hashVal *= 26 instead of 10l=; 26 is the base of the numeric system we're operating, so we end up with fewer collisions

"""
  class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        lo, hi = 1, length-1
        ans = ""
        mod = (10**9) + 7

        def getVal(c):
            return ord(c)-ord('a')+1

        def returnDup(size):
            seen = {}
            start, end = 0, size-1
            hashVal = 0
            hashMap = defaultdict(set)
            for i in range(size): hashVal = (hashVal * 10 + getVal(s[i])) % mod
            while end < length+1:
                if hashVal in hashMap: 
                    newStr = s[start:end+1]
                    for (prevStart, prevEnd) in hashMap[hashVal]:
                        if s[prevStart:prevEnd] == newStr: return newStr
                hashMap[hashVal].add((start, end+1))
                if end+1 == length: break
                hashVal -= (getVal(s[start]) * (10**(size-1))
                hashVal *= 10
                hashVal += getVal(s[end+1])
                hashVal %= mod
                start += 1
                end += 1
            return ""

        while lo <= hi:
            size = lo + ((hi-lo)//2)
            dup = returnDup(size)
            if dup != "":
                ans = dup
                lo = size+1
            else: hi = size-1
        return ans
"""
# size can be very large, so calculating 10**(size-1) is very slow

"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        lo, hi = 1, length-1
        ans = ""

        def returnDup(size):
            seen = {}
            start, end = 0, size-1
            hashVal = 0
            hashMap = defaultdict(list)
            for i in range(size): hashVal = hashVal * 10 + (ord(s[i])-ord('a')+1)
            while end < length+1:
                newStr = s[start:end+1]
                if hashVal in hashMap and newStr in hashMap[hashVal]: return newStr
                hashMap[hashVal].append(newStr)
                if end+1 == length: break
                hashVal -= (ord(s[start])-ord('a')+1) * (10**(size-1))
                hashVal *= 10
                hashVal += (ord(s[end+1])-ord('a')+1)
                start += 1
                end += 1
            return ""

        while lo <= hi:
            size = lo + ((hi-lo)//2)
            dup = returnDup(size)
            if dup != "":
                ans = dup
                lo = size+1
            else: hi = size-1
        return ans
"""
# inefficient operations inside while loop:
#   1. doing newStr = s[start:end+1] takes O(window size) time
#   2. when looking for newStr in hashMap[hashVal], you're looking up key of really long length, which takes O(key) time
#   3. hashMap[hashVal] is a list, not a set

# use capped rolling hash:
#   1. subtract number from left part of the window
#   2. multiply hash value by base
#   3. add on new hashed value for number from right part of window
#   4. take new hash value and mod by 10**9 + 7

# for each hash value, store list of coordinates that hash value occurred at
# to deduce if there is a duplicated string when there is a hash collision, iterate through all coordinates hash has occurred at

# important mod property: A*B % C = ((A%C)*(B%C))%C
