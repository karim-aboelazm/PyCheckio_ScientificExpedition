def remove_brackets(text: str) -> str:
    from itertools import combinations
    brackets, size = ("()", "[]", "{}"), len(text)
    if text in brackets:
        return text
    pairs = [(x, y) for x, y in combinations(range(size), 2)
             if text[x]+text[y] in brackets]
    rb = remove_brackets
    result = [text[x]+rb(text[x+1:y])+text[y]+rb(text[y+1:])
              for x, y in pairs]
    return max(result[::-1], key=len, default='')


if __name__ == '__main__':
    print("Example:")
    print(remove_brackets('(()()'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets('(()()') == '()()'
    assert remove_brackets('[][[[') == '[]'
    assert remove_brackets('[[(}]]') == '[[]]'
    assert remove_brackets('[[{}()]]') == '[[{}()]]'
    assert remove_brackets('[[[[[[') == ''
    assert remove_brackets('[[[[}') == ''
    assert remove_brackets('') == ''
    assert remove_brackets('[(])') == '()'
    print("Coding complete? Click 'Check' to earn cool rewards!")
