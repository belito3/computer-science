class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs, left = 0, 0
        lookup = {}

        for right in range(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]] + 1)
            lookup[s[right]] = right
            rs = max(rs, right - left + 1)
        return rs

    def lengthOfLongestSubstring2(self, s: str) -> int:
        rs, left = 0, 0
        lookup = [None] * 128
        # ord(c): return ASCII value
        for right in range(len(s)):
            if lookup[ord(s[right])] is not None:
                left = max(left, lookup[ord(s[right])] + 1)
            lookup[ord(s[right])] = right
            rs = max(rs, right - left + 1)
        return rs



s = Solution()
# "", abcabcbb, bbbbb, pwwkew, dvdf, dvdfed, dvfex, dvxdfedabcx
#

print(s.lengthOfLongestSubstring("dvxdfedabcx"))
print(s.lengthOfLongestSubstring2("dvxdfedabcx"))