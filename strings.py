# 1. Reverse string
s = input()
print(s[::-1])

# 2. Palindrome string
s = input()
print("Palindrome" if s == s[::-1] else "Not")

# 3. Vowels & consonants
s = input().lower()
vowels = "aeiou"
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print(v, c)

# 4. Uppercase without built-in
s = input()
res = ""
for ch in s:
    if 'a' <= ch <= 'z':
        res += chr(ord(ch)-32)
    else:
        res += ch
print(res)

# 5. Length without len()
s = input()
count = 0
for _ in s:
    count += 1
print(count)

# 6. Anagram
s1 = input()
s2 = input()
print("Anagram" if sorted(s1)==sorted(s2) else "Not")

# 7. First non-repeating
s = input()
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

# 8. Frequency
s = input()
freq = {}
for ch in s:
    freq[ch] = freq.get(ch,0)+1
print(freq)

# 9. Remove duplicates
s = input()
res = ""
for ch in s:
    if ch not in res:
        res += ch
print(res)

# 10. Longest word
s = input()
words = s.split()
longest = max(words, key=len)
print(longest)
