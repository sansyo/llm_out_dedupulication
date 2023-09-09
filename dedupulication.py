# deduplication.py

def lz78_deduplicate(text):
    # LZ78 Deduplication (Simplified version)
    dictionary = {}
    word = ""
    output = ""
    for char in text:
        if word + char not in dictionary:
            if word == "":
                output += char
            else:
                dictionary[word + char] = len(dictionary)
                output += word + char
            word = ""
        else:
            word += char
    return output

def kmp_deduplicate(text):
    # KMP Deduplication (Removes the first longest repeated substring)
    def compute_prefix_function(pattern):
        pi = [0] * len(pattern)
        j = 0
        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
        return pi
    
    prefix_function = compute_prefix_function(text)
    longest_repeated_length = max(prefix_function)
    if longest_repeated_length == 0:
        return text

    position = prefix_function.index(longest_repeated_length)
    repeated_string = text[position-longest_repeated_length+1:position+1]
    return text.replace(repeated_string, '', 1)

def build_suffix_array(string):
    n = len(string)
    suffixes = [(string[i:], i) for i in range(n)]
    suffixes.sort()
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def build_lcp(string, suffix_array):
    n = len(string)
    rank = [0] * n
    for i in range(n):
        rank[suffix_array[i]] = i
    lcp = [0] * (n-1)
    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and string[i+k] == string[j+k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0:
            k -= 1
    return lcp
    
def remove_longest_repeating_substring(string):
    suffix_array = build_suffix_array(string)
    lcp = build_lcp(string, suffix_array)
    if max(lcp) == 0:
        return string
    idx = lcp.index(max(lcp))
    start = suffix_array[idx]
    end = start + max(lcp)
    return string[:start] + string[end:]

if __name__ == "__main__":
    # Test the functions
    text = "圧縮データを短いテキストに変換する圧縮データを短いテキストに変換する圧縮データを短いテキストに変換する"
    print(lz78_deduplicate(text))
    print(kmp_deduplicate(text))
    print(remove_with_suffix_array(text))
