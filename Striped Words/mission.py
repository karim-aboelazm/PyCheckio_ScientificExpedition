def checkio(line: str) -> str:
    Vowels = 'AEIOUY'
    Consonants = 'BCDFGHJKLMNPQRSTVWXZ'
    cont = 0
    newline = ''
    for c in line:
        if c.upper() in Vowels:
            newline += 'a'
        elif c.upper() in Consonants:
            newline += 'b'
        elif not c.isalnum():
            newline += ' '
        else:
            newline += c
    for word in newline.split():
        if 'aa' not in word and 'bb' not in word and word.isalpha() and len(word)>1:
            cont += 1
    return cont

if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
