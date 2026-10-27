def ValidPar(text: str|None) -> bool:
    if not text:
        return True

    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            return False

    return not stack


if __name__ == "__main__":
    print(ValidPar("()[]{}"))

    print(ValidPar(""))

    input_text = "if (a > b) { return a; } else { return b; }"
    text_list=[text for text in input_text if text in ")(][}{" + "\n"]
    text_str = ''.join(text_list)
    print(text_str)
    print(ValidPar(text_str))