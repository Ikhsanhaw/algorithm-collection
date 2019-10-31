def lengthOfLongestSubstring(s):
    lookup_ = set()
    max_ = 0
    length = 0
    for c in s:
        if c not in lookup_:
            length = length + 1
            lookup_.add(c)
        else:
            max_ = max(length, max_)
            length = 0
            lookup_ = set()
    return max_