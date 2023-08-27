def uniqueE(S):
    freq = {}
    for char in S:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    unique_result = []
    for char, count in freq.items():
        if count == 1:
            unique_result.append(char)
    
    return sorted(unique_result)
