import random
from os.path import dirname, join

# Read in all the words in one go
current_dir = dirname(__file__)
file_path = join(current_dir, "./input.txt")
with open(file_path, 'r') as f:
    words = f.read()

# TODO: analyze which words can follow other words

following_words = {}
words = words.split()

for index, word in enumerate(words):
    if word in following_words.keys():
        if index < len(words) - 2:
            following_words[word].append(words[index + 1])
    else:
        if index < len(words) - 2:
            following_words[word] = [words[index + 1]]

# TODO: construct 5 random sentences
# Your code here

start_words = []

stop_punctuation = '.?!"'
stop_words = []


for word in following_words.keys():
    if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
        start_words.append(word)
    elif word[-1] in stop_punctuation:
        stop_words.append(word)

def print_nonsense(num_sentences):
    for i in range(num_sentences):
        # start_word = random.choice(start_words)
        # print(start_word, end=" ")
        # next_word = random.choice(following_words[start_word])
        # print(next_word, end=" ")
        # while next_word not in stop_words:
        #     next_word = random.choice(following_words[next_word])
        #     print(next_word, end=" ")
        # print("\n")
        sentence = ""

        start_word = random.choice(start_words)
        sentence += (" " + start_word)

        next_word = random.choice(following_words[start_word])
        sentence += (" " + next_word)

        """
        This should account for quotations not at the beginning of
        a line. Only checking for closed quotes based on a first
        character of '"' doesn't account for all cases.
        """
        
        while next_word not in stop_words or sentence.count('"') % 2 == 1:
            next_word = random.choice(following_words[next_word])
            sentence += (" " + next_word)
            
        print(sentence)
        print("\n")

print_nonsense(5)

