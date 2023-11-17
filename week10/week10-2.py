class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       return  haystack.find(needle)
    
#########################################################
a = "sadbutsad"
b = "sad"
ans= a.find(b)
print(ans)

a = "leetcode"
b = "leeto"
ans = a.find(b)
print(ans)
