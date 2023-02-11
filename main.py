

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def if_balanced(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            position = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[position] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Небалансированный"
    if len(stack) == 0:
        return "Балансированный"
    else:
        return "Небалансированный"


# Driver code
string0 = '{()}'
print(string0, "-", if_balanced(string0))

string1 = '{()}[{}]'
print(string1, "-", if_balanced(string1))

string2 = '{[{}{}]}[()]'
print(string2, "-", if_balanced(string2))
string3 = '{(})'
print(string3, "-", if_balanced(string3))
string4 = '{[})'       
print(string4, "-", if_balanced(string4))