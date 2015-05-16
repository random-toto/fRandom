#!/usr/bin/python3

import random
import hashlib
import time 

random.seed(hashlib.sha256(str(time.mktime(time.localtime())).encode()).hexdigest())

def rangeRandom(a=0, b=1):
    ''' renvoie un nombre aléatoire entre a et b
    
    '''
    try:
        a = float(a)
        b = float(b)
    except:
        raise ValueError("rangeRandom : a ou b non réels.")
    assert a < b
    return a + (b - a)*(random.random())

def multipleRandom(n=1, a=0, b=1):
    '''
    '''
    try:
        n = int(n)
    except:
        raise ValueError("multipleRandom : Pas un int.")
    return [rangeRandom(a, b) for i in range(n)]

