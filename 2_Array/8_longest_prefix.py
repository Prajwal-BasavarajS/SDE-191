def longest_prefix(strs):
    min_length = float('inf')

    for s in strs :
        if len(s) < min_length:
            min_length = len(s)

    i = 0

    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1

    return s[:1]

print(longest_prefix(["flower","floe","floweree"]))


def longest_prefix(strs):
    if not strs:
        return ""

    min_length = float('inf')

    for s in strs:
        if len(s) < min_length:
            min_length = len(s)

    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return strs[0][:i]
        i += 1

    return strs[0][:min_length]


print(longest_prefix(["flower", "floe", "floweree"]))
