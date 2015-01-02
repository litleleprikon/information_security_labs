#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'litleleprikon'


from frequency_counter import FrequencyCounter


def comparator(stat, current):
    encode_dictionary = {}
    for i, enc_letter in enumerate(current):
        encode_dictionary[enc_letter] = stat[i]
    return encode_dictionary


def decrypt(text, dictionary):
    decrypted = []
    for letter in text:
        decrypted.append(dictionary[letter])
    return ''.join(decrypted)


def decrypt_text(file_name):
    statistic = FrequencyCounter.load_from_file('stat.json')
    counter = FrequencyCounter()
    counter.count_from_file(file_name)
    counter.sort()
    with open(file_name) as file:
        text = file.read()
    dictionary = {pair[0]: statistic[i][0] for i, pair in enumerate(counter.sorted)}
    return decrypt(text, dictionary)


def main():
    with open('decrypted.txt', 'w') as file:
        file.write(decrypt_text('encrypt14.txt'))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")