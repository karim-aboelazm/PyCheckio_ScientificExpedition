from unicodedata import normalize, category

def checkio(in_string):

    return ''.join(c for c in normalize('NFD', in_string) if category(c) != 'Mn')

if __name__ == '__main__':
    assert checkio(u"pr�f�rent") == u"preferent"
    assert checkio(u"loa?i tr?n l??n") == u"loai tran lon"
    print('Done')
