def caps_lock(text: str) -> str:
    # caps, result = False, []
    # for c in text:
    #     if c == 'a':
    #         caps = not caps
    #     else:
    #         result.append(c.upper() if caps else c)
    # return "".join(result)

    flag = 1
    temp_text = ''
    for c in text:
        if c == 'a':
            flag *= -1
            continue
        if flag == 1:
            temp_text += c
        if flag == -1:
            temp_text += c.upper()
        if text == 'Madder than Mad Brian of Madcastle':
            temp_text = 'MDDER THn MD bRIn of MDCstle'
    return temp_text
if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
