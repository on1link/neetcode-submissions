class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        seen = defaultdict(int)

        for c in magazine:
            seen[c] += 1
        
        for c in ransomNote:
            if seen[c] > 0:
                seen[c] -= 1
            else:
                return False

        return True