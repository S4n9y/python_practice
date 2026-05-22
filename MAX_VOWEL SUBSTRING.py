class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = "aeiou"

        # Count vowels in first window
        cur_vowels = 0

        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1

        max_vowels = cur_vowels

        # Slide the window
        for i in range(k, len(s)):

            # Remove left character
            if s[i - k] in vowels:
                cur_vowels -= 1

            # Add new right character
            if s[i] in vowels:
                cur_vowels += 1

            max_vowels = max(max_vowels, cur_vowels)

        return max_vowels