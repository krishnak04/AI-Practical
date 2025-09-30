from collections import deque

def is_oneletter_diff(word1, word2):
    diffcount = sum(1 for a, b in zip(word1, word2) if a != b)
    return diffcount == 1

def word_ladder(start, end, word_list):
    word_set = set(word_list)
    if end not in word_set:
        return None

    queue = deque([(start, [start])])
    visited = set([start])  # Track visited words to avoid loops

    while queue:
        current_word, path = queue.popleft()
        if current_word == end:
            return path

        # Go through all words in the dictionary
        for word in word_set.copy():
            if word not in visited and is_oneletter_diff(current_word, word):
                visited.add(word)
                queue.append((word, path + [word]))

    return None

# Sample test
dictionary = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
start_word = 'hit'
end_word = 'cog'

result = word_ladder(start_word, end_word, dictionary)
print('Word ladder path:', result)
