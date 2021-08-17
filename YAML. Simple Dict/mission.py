def yaml(a):
    dic = {}
    a = list(x for x in sorted(a.split('\n')) if x != '')
    for x in a:
        try:
            dic[x.split(': ')[0]] = int(x.split(': ')[1])
        except:
            dic[x.split(': ')[0]] = x.split(': ')[1]
    return dic

if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
