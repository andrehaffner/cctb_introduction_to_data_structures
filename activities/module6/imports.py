import string


def lowercase(st): return st.lower()


def uppercase(st): return st.upper()


def number_removal(st): return ''.join([c for c in st if not c.isdigit()])


def punctuation_removal(st): return ''.join([c for c in st if c not in string.punctuation])


def white_space_removal(st): return st.replace(' ', '')
