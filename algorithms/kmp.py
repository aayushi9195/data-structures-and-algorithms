"""
https://www.youtube.com/watch?v=GTJr8OvyEVQ
https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

Core idea: Do not start from the beginning of pattern when there is a character mismatch

Runtime complexity: O(m + n) where m is length of text and n is length of pattern
Space complexity: O(n)
"""


def compute_temporary_array(pattern):
    lps = [0] * len(pattern)
    index, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[index]:
            lps[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = lps[index-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_substring_search(text, pattern):
    lps = compute_temporary_array(pattern)
    i, j = 0, 0
    while i < len(text) and j < len(pattern):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    if j == len(pattern):
        return True
    return False


def main():
    text = "abcxabcdabcdabcy"
    pattern = "abcdabcy"
    print('Result:', kmp_substring_search(text, pattern))
    pattern = "abcdabcyx"
    print('Result:', kmp_substring_search(text, pattern))


if __name__ == '__main__':
    main()





