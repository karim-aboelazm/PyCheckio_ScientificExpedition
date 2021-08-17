def checkio(line1: str, line2: str) -> str:
    line1 = line1.split(',')
    line2 = line2.split(',')
    new_line = [x for x in line2 if x in line1]
    return ','.join(sorted(new_line))


if __name__ == '__main__':
    print("Example:")
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three',
 'four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
