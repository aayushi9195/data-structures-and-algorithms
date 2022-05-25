"""
https://www.youtube.com/watch?v=H4VrKHVG5qI
https://github.com/mission-peace/interview/blob/master/src/com/interview/string/RabinKarpSearch.java

Time complexity: O(m*n) if the hash function is bad
Space complexity: O(1)

Applications:
Detecting plagiarism
Finding multiple patterns of same length in the text
"""

from math import pow

prime = 101


def pattern_search(text, pattern):
    n, m = len(text), len(pattern)
    pattern_hash = create_hash(pattern, m)
    text_hash = create_hash(text, m)
    for i in range(1, n-m+2):
        if pattern_hash == text_hash and check_equal(text, i - 1, i + m - 2, pattern, 0, m - 1):
            return i - 1
        if i < n - m + 1:
            text_hash = recalculate_hash(text, i - 1, i + m - 1, text_hash, m)
    return -1


def recalculate_hash(text, old_index, new_index, old_hash, pattern_length):
    new_hash = old_hash - ord(text[old_index])
    new_hash = new_hash / prime
    new_hash += ord(text[new_index]) * pow(prime, pattern_length-1)
    return new_hash


def check_equal(text, tstart, tend, pattern, pstart, pend):
    if tend - tstart != pend - pstart:
        return False
    while tstart <= tend and pstart <= pend:
        if text[tstart] != pattern[pstart]:
            return False
        tstart += 1
        pstart += 1
    return True


def create_hash(str, end):
    hash = 0
    # The ord() function returns the number representing the unicode code of a specified character
    for i in range(end):
        hash += ord(str[i]) * pow(prime, i)
    return hash


def main():
    text = "TusharRoy"
    print(pattern_search(text, "sharRoy"))
    print(pattern_search(text, "Roy"))
    print(pattern_search(text, "shas"))
    print(pattern_search(text, "usha"))
    print(pattern_search(text, "Tus"))


if __name__ == '__main__':
    main()