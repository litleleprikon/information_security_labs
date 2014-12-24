#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'


class GCounterCipher:
    def __init__(self):
        with open('passwords.txt', 'r') as file:
            self._keys = [line[:-1] for line in file.readlines()]
        self.char_map = [chr(x) for x in range(32, 127)]
        self.map_len = len(self.char_map)

    def encrypt_once(self, key, text):
        result = []
        key_len = len(key)
        for i, symbol in enumerate(text):
            res_symbol_code = (self.char_map.index(symbol) + ord(key[i % key_len])) % self.map_len
            res_symbol = self.char_map[res_symbol_code]
            result.append(res_symbol)
        return ''.join(result)

    def encrypt(self, file_name):
        with open(file_name, 'r') as file:
            text = file.read()
            for key in self._keys:
                text = self.encrypt_once(key, text)
        with open('encrypted.txt', 'w') as file:
            file.write(text)

    def decrypt_once(self, key, text):
        result = []
        key_len = len(key)
        for i, symbol in enumerate(text):
            res_symbol_code = (self.char_map.index(symbol) - ord(key[i % key_len])) % self.map_len
            res_symbol = self.char_map[res_symbol_code]
            result.append(res_symbol)
        return ''.join(result)

    def decrypt(self):
        with open('encrypted.txt', 'r') as file:
            text = file.read()
            for key in reversed(self._keys):
                text = self.decrypt_once(key, text)
        with open('decrypted.txt', 'w') as file:
            file.write(text)


def main():
    cipher = GCounterCipher()
    cipher.encrypt('text.txt')
    cipher.decrypt()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")