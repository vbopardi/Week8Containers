import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    The two strings to the right of the in keyword above are equal
    but not equal *representationally*.
    In particular, the first is in NFC form, and the second is in NFD form.
    The purpose of this class is to automatically normalize our strings for us,
    making foreign languages "just work" a little bit easier.
    '''

    def __init__(self, text, normal_form='NFC'):
        self.text = unicodedata.normalize(normal_form, text)
        self.normal_form = normal_form
        pass

    def __repr__(self):
        '''
        The string returned by the __repr__ function should be valid python
        that can be substituted directly into the python interprete
        '''

        t = str(self.text)
        nf = str(self.normal_form)

        return "NormalizedStr('" + t + "', '" + nf + "')"

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string object.
        The output is similar, but not exactly the same, as the __repr__
        '''

        return str(self.text)

    def __len__(self):
        '''
        Returns the length of the string.
        The expression `len(a)` desugars to a.__len__().
        '''

        return len(self.text)

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        The expression `a in b` desugars to `b.__contains__(a)`.

        '''

        nsubstr = unicodedata.normalize(self.normal_form, substr)

        if nsubstr in self.text:
            return True

        return False

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        The expression `a[b]` desugars to `a.__getitem__(b)`.
        '''

        return self.text[index]

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''

        return str(self.text).lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''

        return str(self.text).upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        The expression `a + b` gets desugared into `a.__add__(b)`.

        HINT:
        '''

        nnb = self.text + str(b)
        nnbn = unicodedata.normalize(self.normal_form, nnb)

        return NormalizedStr(nnbn)

    def __iter__(self):
        '''
        HINT:
        '''

        return Iterator(self.text)


class Iterator:
    def __init__(self, text):
        self.text = text
        self.ct = 0

    def __next__(self):
        if len(self.text) <= self.ct:
            raise StopIteration
        else:
            idx = self.text[self.ct]
            self.ct += 1
            return idx
