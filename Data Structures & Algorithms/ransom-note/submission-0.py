class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for char in ransomNote:
            if char in count and count[char] > 0:
                count[char] -= 1
            else:
                return False
        return True
