#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'


from random import randint


N = 13243
ALPHABET = [x for x in range(48, 57)]
ALPHABET.extend([x for x in range(97, 122)])

with open('passwords.txt', 'w') as file:
    file.writelines((''.join([chr(ALPHABET[(randint(0, len(ALPHABET)-1))]) for _ in range(randint(3, 10))])+'\n') for _ in range(N))
