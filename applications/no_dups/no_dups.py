from collections import OrderedDict

def no_dups(s):
    # return " ".join(set(s.split()))
    # return " ".join(list(set(s.split())))
    cache = {}
    for word in s.split():
        cache[word] = None
    return " ".join(cache.keys())


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))