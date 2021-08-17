from itertools import zip_longest

def find_start(text, word):

    start_pos = text.find(word)
    if start_pos >= 0:
        line_number = text.count('\n', 0, start_pos)
        line_start = text.rfind('\n', 0, start_pos)
        row_start = line_number + 1
        column_start = start_pos - line_start
        return row_start, column_start

def checkio(text, word):
    text = text.replace(' ', '').lower()
    distance = len(word) - 1
    start = find_start(text, word)
    if start:
       row_start, column_start = start
       return [row_start, column_start, row_start, column_start + distance]
    else:
        text = '\n'.join(''.join(x) for x in zip_longest(*text.split('\n'), fillvalue=''))
        start = find_start(text, word)
        column_start, row_start = start
        return [row_start, column_start, row_start + distance, column_start]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
