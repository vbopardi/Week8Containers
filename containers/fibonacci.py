def fibs(n):
    '''
    This function computes the first n fibonacci numbers.
    Notice that this function uses O(n) memory.
    '''
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    '''
    This function computes the n-th fibonacci number,
    but it uses O(n) memory to do so,
    which is bad.
    '''
    return fibs(n)[-1]


def fib(n):
    '''
    This function computes the n-th fibonacci number,
    but it consumes only O(1) memory,
    and is optimal.
    '''
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''

    def __init__(self, n=None):
        self.n = n

    def __repr__(self):
        if self.n is None:
            return "Fib()"
        else:
            return "Fib(" + str(self.n) + ")"

    def __iter__(self):
        return FibIter(self.n)


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''

    def __init__(self, n):
        self.n = n
        self.counter = 0
        self.first = 1
        self.sec = 1
        self.next = None

    def __next__(self):
        if self.n and self.n <= self.counter:
            raise StopIteration

        elif self.counter < 2:
            self.counter += 1
            return 1
        else:
            self.counter += 1
            self.next = self.first + self.sec
            self.first = self.sec
            self.sec = self.next
            return self.next


def fib_yield(n=None):
    '''
    If n is None, then the generator is infinite.
    '''

    first = 1
    sec = 1

    if n is None:
        yield first
        yield sec
        f1 = first
        f2 = sec
        while True:
            i = f1 + f2
            yield i
            f1 = f2
            f2 = i
    elif n == 1:
        yield first
    else:
        yield first
        yield sec
        counter = n - 2
        f1 = first
        f2 = sec
        while counter > 0:
            i = f1 + f2
            yield i
            f1 = f2
            f2 = i
            counter -= 1
