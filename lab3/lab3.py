def to_str(nested_list):
    result = []
    while nested_list:
        element = nested_list.pop()
        if isinstance(element, list):
            nested_list.extend(element)
        else:
            result.append(str(element))
    return ' -> '.join(reversed(result)) + ' -> None'
print(to_str([1, [2, [3, [4, [5]]]]]))

def to_str_rec(nested_list):
    def recursion(nested_list):
        if not nested_list:
            return []
        else:
            first = nested_list[0]
            rest = nested_list[1:]
            if isinstance(first,list):
                return recursion(first)+recursion(rest)
            else:
                return [first]+ recursion(rest)
    return ' -> '.join(map(str,recursion(nested_list)))+ ' -> None'
print(to_str_rec([1, [2, [3, [4, [5]]]]]))


def calc_req(n):
    if n == 0 or n == 1:
        return 1
    return calc_req(n - 2) + (calc_req(n - 1) / (2 ** (n - 1)))
print(f'a(2) == {calc_req(2)}')


def calc(n):
    if n == 0 or n == 1:
        return 1
    a1=1
    a2=1
    for i in range(2,n+1):
        current=a1+(a2/(2**(i-1)))
        a1=a2
        a2=current
    return a2
print(f'a(2) == {calc(2)}')
