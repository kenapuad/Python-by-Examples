name = input("Name: ")
vowel = ['a','e','i','o','u']

count = 0

name = name.lower()

for i in name:
    if i in vowel:
        count = count + 1

print(f"Your name has {count} vowels")