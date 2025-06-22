num = int(input("Enter a number: "))

# Reverse
reverse = 0
original = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check if palindrome
if original == reverse:
    print(original, "is a Palindrome Number.")
else:
    print(original, "is not a Palindrome Number.")
