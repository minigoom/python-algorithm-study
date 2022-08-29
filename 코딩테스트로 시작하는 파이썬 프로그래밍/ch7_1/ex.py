
def invert_dictionary(d):
    inverted={}
    for key in d:
        num = d[key]
        if not num in inverted:
            inverted[num] = key
        else:
            inverted[num].append(key)

    return inverted

d = {'a':1,'b':1,'c':1}
invert_dictionary(d)