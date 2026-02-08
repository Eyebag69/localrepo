# Program to count words in a sentence without using split()

sentence = input("Enter a sentence: ")

count = 0
in_word = False  # flag to check if we are inside a word

for char in sentence:
    if char != " ":  # when it's not a space
        if not in_word:   # we are entering a new word
            count += 1
            in_word = True
    else:
        in_word = False   # we hit a space, so end of word

print("Number of words:", count)
         