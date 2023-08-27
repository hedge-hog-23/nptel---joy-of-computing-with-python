def count_letters(S):
    freq = {}
    for char in S:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
