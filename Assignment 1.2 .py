# Taking two string inputs
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

combined = str1 + str2
print("\nCombined string:", combined)

print("Uppercase:", combined.upper())
print("Lowercase:", combined.lower())
print("Title Case:", combined.title())
print("Reversed:", combined[::-1])
print("Length of combined string:", len(combined))
print("Does it contain 'a'?", 'a' in combined)
print("Replace 'a' with '@':", combined.replace('a', '@'))
