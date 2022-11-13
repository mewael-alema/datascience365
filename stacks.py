def balanced_brackets(s):
    stack = []
    d = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
        }


    for char in s:
        if not stack:
            stack.append(char)
        elif char not in d:
            stack.append(char)
        elif d[char] == stack[-1]:
                stack.pop()
        else:
            stack.append(char)
    
    if not stack:
        return True
    
    else:
        return False
