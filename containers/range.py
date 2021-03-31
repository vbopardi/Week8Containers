def range(a, b=None, c=None):
    if b and c:
        if b > 0 and c > b:
            yield 0
        elif b/c < 0:
            return []
        elif b < 0 and c < 0:
            i = 0
            while i > b:
                yield i
                i += c
        else:
            i = 0
            while i < b:
                yield i
                i += c

    elif b is None and c is None:
        if a <= 0:
            return []
        else:
            i = 0
            while i < a:
                yield i
                i += 1

    elif c is None:
        if a >= b:
            return []
        else:
            i = a
            while i < b:
                yield i
                i += 1
