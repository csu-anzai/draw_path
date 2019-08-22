# print(5 % 2)

# test stack

def reverse_str_stack(strs):
    l = list(strs)
    result = ''
    while len(l) > 0:
        result += l.pop()
    return result


if __name__ == '__main__':
    strs = 'abc'
    new_str = reverse_str_stack(strs)
    print(new_str)
