from typing import Tuple

def follow(instructions: str) -> Tuple[int, int]:
    forward = instructions.count('f')
    left = instructions.count('l')
    right = instructions.count('r')
    back = instructions.count('b')
    return (right-left,forward-back)

if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
