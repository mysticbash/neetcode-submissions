class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            if s.count(alphabet[i])!=t.count(alphabet[i]):
                return False
                break
        return True