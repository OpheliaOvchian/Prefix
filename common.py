def common(strings):
    result = []
    strings.sort()

    first = [i for i in strings[0]]
    last = [i for i in strings[-1]]

    for i in range(len(first)):
        if i >= len(last) or first[i] != last[i]:
            break
        result.append(first[i])

    prefix = ''.join(result)
    return prefix

string = ["asbba", "aser", "astir", "asbsd"]
prefix = common(string)
print(prefix)