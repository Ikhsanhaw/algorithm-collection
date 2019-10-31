def longestPalindrome(s):

    def isPalindrome(s):
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True

    if len(s) == 1 or isPalindrome(s):
        return s
    s1 = longestPalindrome(s[1:])
    s2 = longestPalindrome(s[:-1])
    s3 = longestPalindrome(s[1:-1])
    return s1 if len(s1) >= len(s2) and len(s1) >= len(s3) else s2 if len(
        s2) >= len(s3) else s3