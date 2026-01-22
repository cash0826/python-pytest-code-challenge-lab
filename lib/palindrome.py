def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s
    
    start = 0
    max_len = 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # length of the palindrome
    
    for i in range(n):
        len1 = expand_around_center(i, i)      # Odd length palindromes
        len2 = expand_around_center(i, i + 1)  # Even length palindromes
        curr_len = max(len1, len2)
        
        if curr_len > max_len:
            max_len = curr_len
            start = i - (curr_len - 1) // 2
            
    return s[start:start + max_len]