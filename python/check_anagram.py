def check_anagram(str1, str2):
    return "".join(sorted(str1.lower())) == "".join(sorted(str2.lower()))