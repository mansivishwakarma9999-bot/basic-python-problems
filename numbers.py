# 1. Prime Number
n = int(input("Enter number: "))
is_prime = True
if n < 2:
    is_prime = False
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")


# 2. Factorial
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)


# 3. Palindrome Number
n = input("Enter number: ")
print("Palindrome" if n == n[::-1] else "Not Palindrome")


# 4. Sum of digits
n = input("Enter number: ")
sum_digits = 0
for digit in n:
    sum_digits += int(digit)
print(sum_digits)


# 5. Divisors
n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")


# 6. Armstrong Number
n = int(input("Enter number: "))
temp = n
order = len(str(n))
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
print("Armstrong" if sum == n else "Not Armstrong")


# 7. Prime in range
start = int(input())
end = int(input())
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)


# 8. GCD & LCM
a = int(input())
b = int(input())

# GCD
while b:
    a, b = b, a % b
gcd = a

# LCM
lcm = (a * b) // gcd

print("GCD:", gcd, "LCM:", lcm)


# 9. Decimal to Binary
n = int(input())
binary = ""
while n > 0:
    binary = str(n % 2) + binary
    n //= 2
print(binary)


# 10. Perfect Number
n = int(input())
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
print("Perfect" if sum == n else "Not Perfect")
