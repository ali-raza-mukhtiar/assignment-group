✅ 1. From 'DataScience'
text = "DataScience"

print(text[:4])      # Data
print(text[4:])      # Science
print(text[1:7])     # ataSci
✅ 2. From 'Programming' (negative indexing)
word = "Programming"

print(word[-3:])     # ing
print(word[-7:-3])   # gram
✅ 3. From 'ABCDEFGHIJ'
text = "ABCDEFGHIJ"

print(text[::2])     # every 2nd char
print(text[::3])     # every 3rd char
print(text[::-1])    # reverse
✅ 4. User Input
text = input("Enter a string: ")

print(text[:3])          # first 3
print(text[-3:])         # last 3
print(text[3:-3])        # middle part
✅ 5. Reverse each word
text = "Python is fun"

words = text.split()
reversed_words = [word[::-1] for word in words]

print(" ".join(reversed_words))   # nohtyP si nuf
