#!/usr/bin/python3

"""

The module function: text_indentation().

make test: python3 -m doctest -v ./tests/5-text_indentation.txt

"""


def text_indentation(text):
    """

    add /n to text

    Arguments:
    text: string

    """
    err = "text must be a string"
    if not isinstance(text, str):
        raise TypeError(err)

    if text is None:
        raise TypeError(err)

    if len(text) < 0:
        raise TypeError(err)

    text = text.replace('.', '.\\')
    text = text.replace('?', '?\\')
    text = text.replace(':', ':\\')

    print('\n\n'.join([t.strip() for t in text.split('\\')]), end="")
