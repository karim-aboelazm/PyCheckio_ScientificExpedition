VOWELS = "aeiouy"

def translate(phrase):
    new_phrase = ''
    skip = 0
    for x in phrase:
        if x in VOWELS and skip == 0:
            new_phrase += x
            skip = 3
        elif x not in VOWELS and skip == 0 and x != ' ':
            new_phrase += x
            skip = 2
        elif x == ' ':
            new_phrase += x
            skip += 1
        skip -= 1
    return new_phrase


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
