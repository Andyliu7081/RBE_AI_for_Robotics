def isreverse(s1, s2):
    # Your code here
    # if both strings are empty
    if not s1 and not s2:
        return True

    # If different, no reverse
    if len(s1) != len(s2):
        return False

    # last character
    return s1[0] == s2[-1] and isreverse(s1[1:], s2[:-1])

# Example output
# print("<empty>, <empty> -> ", isreverse("", "")) # True
# print("a, a -> ", isreverse("a", "a")) # True
# print("ab, ba -> ", isreverse("ab", "ba")) # True
# print("abc, cba -> ", isreverse("abc", "cba")) # True
# print("abcd, cba -> ", isreverse("abcd", "cba")) # False
