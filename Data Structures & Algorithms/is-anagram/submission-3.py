class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        memo = [0] * 26
        
        for c in s:
            memo[(ord(c)-ord('a'))] += 1
        
        for c in t:
            memo[(ord(c)-ord('a'))] -= 1
        
        for num in memo:
            if num != 0:
                return False
        
        return True