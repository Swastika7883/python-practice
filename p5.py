#28. Find the Index of the First Occurrence in a String


#Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        
        return -1


# -------- DRIVER CODE --------
if __name__ == "__main__":
    haystack = input("Enter haystack string: ")
    needle = input("Enter needle string: ")

    sol = Solution()  # sol is an obj 
    result = sol.strStr(haystack, needle)

    print("Output:", result)


        # remember when variable stores a class(), its called obj
        #u need obj to used the func of te class
        # obj = classname()
        #a = obj.func(a1,a2)