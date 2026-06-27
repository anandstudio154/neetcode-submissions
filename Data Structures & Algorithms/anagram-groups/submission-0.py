class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freq(s):
            fq = [0]*26
            for i in s:
                fq[ord(i)-ord('a')] += 1
            return tuple(fq)
        frequency = dict()
        for i in strs:
            if freq(i) in frequency:
                frequency[freq(i)].append(i)
            else:
                frequency[freq(i)] = [i]
        return list(frequency.values())