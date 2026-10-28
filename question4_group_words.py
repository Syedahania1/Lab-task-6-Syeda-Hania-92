words = ["apple", "ant", "banana", "ball", "cat"]

grouped_words = {}

for word in words:
    first_letter = word[0]

    if first_letter in grouped_words:
        grouped_words[first_letter].append(word)
    else:
        grouped_words[first_letter] = [word]

print(grouped_words)
