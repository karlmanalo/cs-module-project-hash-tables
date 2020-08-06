import re

def word_count(s):

    count = {}
    
    punctuation = '":;,.-+=/\|[]{}()*^&'

    for char in s:
        if char in punctuation:
            s = s.replace(char, "")

    for word in s.lower().split():
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    return count
        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))