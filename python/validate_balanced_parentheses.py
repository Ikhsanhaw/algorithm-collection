def isValid(s):
    stack_ = []
    kv = {'}': '{', ']': '[', ')': '('}

    for c in s:
        if c in kv.values():
            stack_.append(c)
        else:
            c_ = stack_.pop()
            if kv.get(c) != c_:
                return False
    return len(stack_) == 0