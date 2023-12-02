#!/usr/bin/python3


def multiple_returns(sentence):

    """returns the length of the sentence and the first character"""

    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
