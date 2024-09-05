# Counts charicters in string
def count_chars(text):
    return len(text)

# Counts words in string
def count_words(text):
    return len(text.split())

# Counts sentences in string
def count_sentences(text):
    return text.count(".") + text.count("!") + text.count("?")