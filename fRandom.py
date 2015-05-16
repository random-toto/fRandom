#!/usr/bin/python3

def rangeRandom(a=0, b=1):
    ''' renvoie un nombre aléatoire entre a et b
    
    '''
    try:
        a = float(a)
        b = float(b)
    except:
        raise ValueError("rangeRandom : a ou b non réels.")
    assert a < b
    import random
    import hashlib
    import time 
    random.seed(hashlib.sha256(str(time.mktime(time.localtime())).encode()).hexdigest())
    return a + (b - a)*(random.random())

