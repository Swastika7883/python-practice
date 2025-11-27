class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)  # strings are immutable
        
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            
            s[i], s[j] = s[j], s[i]  # swap
            i += 1
            j -= 1
        
        return "".join(s)


# -------- DRIVER CODE --------
if __name__ == "__main__":
    s = input("Enter a string: ")

    sol = Solution()
    result = sol.reverseVowels(s)

    print("Output:", result)
