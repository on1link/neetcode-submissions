class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        seen = defaultdict(int)
        seen_r = defaultdict(int)

        for c in magazine:
            seen[c] += 1
        
        for c in ransomNote:
            seen_r[c] += 1

        for c in seen_r:
            if c not in seen or seen[c] < seen_r[c]:
                return False

        return True