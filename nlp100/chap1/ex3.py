s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

words = s.split(' ')

for (i, word) in enumerate(words):
    if ',' in word:
        word = word.strip(',')
    if '.' in word:
        word = word.strip('.')
    
    words[i] = word

word_len_list = []
for word in words:
    word_len = len(word)
    word_len_list.append(word_len)