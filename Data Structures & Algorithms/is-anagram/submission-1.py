class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for i in s:
            freq[ord(i)-ord('a')] += 1
        for t in t:
            freq[ord(t)-ord('a')] -= 1
        return freq==[0]*26
        