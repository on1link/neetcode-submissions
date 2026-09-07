class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
            
        count = {}
        for c in ransomNote:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        count_m = {}
        for c in magazine:
            if c in count_m:
                count_m[c] += 1
            else:
                count_m[c] = 1
        
        for c in ransomNote:
            if c not in magazine:
                return False
            if count[c] > count_m[c]:
                return False

        return True