words = input("Please enter 10 words.")
words = words.split()
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
x = []
for word in words:
    if word[0] in vowels:
        x.append(word)
print(x)


