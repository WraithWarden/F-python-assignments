def filter_long_words(words, n):
    result = []

    for word in words:
        if len(word) > n:
            result.append(word)

    return result


words = ["apple", "banana", "cat", "watermelon", "dog"]

print(filter_long_words(words, 4))