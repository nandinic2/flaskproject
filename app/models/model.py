##function
str = "hello"

def reverse(word):
    arr = []
    count = len(word)
    for s in word:
        count -= 1
        arr.append(word[count])
    word = "".join(arr)
    return word


print(reverse(str))

def shout(word):
    return word.upper()

print(shout(str))


def flipit(string):
    newstring = ""
    for n in string:
        newstring = n + newstring
    return newstring

print(flipit(str))
