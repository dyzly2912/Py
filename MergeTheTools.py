import textwrap

def merge_the_tools(string, k):
    parts = textwrap.wrap(string, k)
    for part in parts:
        seen = set()
        output = []
        for ch in part:
            if ch not in seen:
                seen.add(ch)
                output.append(ch)
        print(''.join(output))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)