text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        " Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = text.split()
new_string = []
for word in words:
    if ',' in word:
        index_comma = word.index(',')
        new_word_comma = word[:index_comma] + 'ing' + word[index_comma:]
        new_string.append(new_word_comma)
    elif '.' in word:
        index_dot = word.index('.')
        new_word_dot = word[:index_dot] + 'ing' + word[index_dot:]
        new_string.append(new_word_dot)
    else:
        new_string.append(word + 'ing')

print(' '.join(new_string))
