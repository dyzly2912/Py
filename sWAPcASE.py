def swap_case(s):
    result = []
    for char in s:
        if char == char.lower():
            result.append(char.upper())
        elif char == char.upper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)