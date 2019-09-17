#!/usr/bin/python3
def multiple_returns(sentence):
        length = len(sentence)
        first = sentence[0]
        if sentence == "":
                return(None)
        else:
                return(len(sentence), sentence[0])
