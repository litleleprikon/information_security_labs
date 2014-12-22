#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'

from random import randint

ALPHABET = [x for x in range(48, 57)]
ALPHABET.extend([x for x in range(97, 122)])


def random_symbol():
    index = randint(0, len(ALPHABET)-1)
    return chr(ALPHABET[index])


def pass_gen(n):
    result = []
    for i in range(n):
        result.append(random_symbol())
    return ''.join(result)


def main():
    for i in range(20):
        print(pass_gen(4))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")