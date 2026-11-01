def find_longest_word(words):
    longest_length = 0

    for word in words:
        current_length = len(word)

        if current_length > longest_length:
            longest_length = current_length

    return longest_length


words = ["apple", "banana", "watermelon", "mango"]

result = find_longest_word(words)
print(result)