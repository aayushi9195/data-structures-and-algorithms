"""
https://www.youtube.com/watch?v=CpZh4eF8QBw
https://github.com/mission-peace/interview/blob/master/src/com/interview/string/ZAlgorithm.java

Core idea: Create an array Z where Z[k] = longest substring starting at k which is also a prefix of the string

Time complexity - O(n + m)
Space complexity - O(n + m)
"""


def calculate_z(input):
    z = [0] * len(input)
    left, right = 0, 0
    for k in range(1, len(input)):
        if k > right:
            left = right = k
            while right < len(input) and input[right] == input[right - left]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            # We are operating inside the box
            k1 = k - left
            # If value does not stretches till right bound then just copy it
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            # Otherwise try to see if there are more matches
            else:
                left = k
                while right < len(input) and input[right] == input[right - left]:
                    right += 1
                z[k] = right - left
                right -= 1
    return z


def z_match_pattern(text, pattern):
    new_string = pattern + '$' + text
    z_array = calculate_z(new_string)
    result = []
    for ind, val in enumerate(z_array):
        if val == len(pattern):
            result.append(ind - len(pattern) - 1)
    return result


def main():
    text = "aaabcxyzaaaabczaaczabbaaaaaabc"
    pattern = "aaabc"
    print('Result:', z_match_pattern(text, pattern))
    pattern = "aaabe"
    print('Result:', z_match_pattern(text, pattern))


if __name__ == '__main__':
    main()