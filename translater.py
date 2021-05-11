import random

def weirdify(text):
    ret = ''
    #get char list
    f = open('chars.txt', 'r', encoding='utf8')
    read = f.read()
    char = read.split('\n')
    charlist = []
    for c in char:
        charlist.append(c.split(':')[1].split(','))

    #change 
    for c in text:
        index = ord(c)
        if index >= 65 and index <= 90:
            index -= 65
            ret += random.choice(charlist[index])
        elif index >= 97 and index <= 122:
            index -= 71
            ret += random.choice(charlist[index])
        else:
            ret += c
    
    return ret

weirdify('hello world')