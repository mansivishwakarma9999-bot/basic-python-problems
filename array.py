arr = list(map(int, input().split()))

# 1. Max & Min
print(max(arr), min(arr))

# 2. Sum
print(sum(arr))

# 3. Reverse
print(arr[::-1])

# 4. Second largest
arr.sort()
print(arr[-2])

# 5. Even & Odd
even = odd = 0
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)

# 6. Two sum
target = int(input())
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])

# 7. Move zeros
res = [x for x in arr if x != 0] + [0]*arr.count(0)
print(res)

# 8. Duplicates
seen = set()
dup = set()
for x in arr:
    if x in seen:
        dup.add(x)
    seen.add(x)
print(dup)

# 9. Merge sorted arrays
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sorted(a+b))

# 10. Missing number (1 to n)
n = int(input())
arr = list(map(int, input().split()))
total = n*(n+1)//2
print(total - sum(arr))
