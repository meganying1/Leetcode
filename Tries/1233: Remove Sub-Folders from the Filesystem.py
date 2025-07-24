# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# topics: array, string, depth-first search, trie
# difficulty: medium

# problem:
# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
#   For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode(None)

    def isSubfolder(self, folder):
        curr = self.trie
        for f in folder.split('/')[1:]:
            currFolders = curr.children
            if f in currFolders:
                if None in currFolders[f].children: return True
                else: curr = currFolders[f]
            else: return False

    def addFolder(self, folder):
        curr = self.trie
        for f in folder.split('/')[1:]:
            currFolders = curr.children
            if f not in currFolders:
                currFolders[f] = TrieNode(f)
            curr = currFolders[f]
        curr.children[None] = None

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        folder.sort()
        for f in folder:
            if not directory.isSubfolder(f):
                ans.append(f)
                directory.addFolder(f)
        return ans

# time complexity: O(n*L*logn), where n is the number of folders and L is the maximum length of a folder path
#   sorting takes O(nlogn) steps, but each comparison can involve up to L characters
#   going through each folder path takes O(n*L) time
#     for each folder path, parsing the path and checking if it's a subfolder or adding it to the directory takes O(L) time
# space complexity: O(n*L)
#   each folder path creates up to L trie nodes and we have n folders
