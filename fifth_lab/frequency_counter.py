#!/usr/bin/env python
# -*- coding:utf-8 -*-
from itertools import count

__author__ = 'litleleprikon'


import json


class FrequencyCounter:
    def __init__(self):
        self.letters = {}
        self.sorted = None

    def count_from_file(self, file_name):
        with open(file_name) as file:
            self.count(file.read())

    def add(self, letter):
        if self.letters.get(letter) is None:
            self.letters[letter] = 1
        else:
            self.letters[letter] += 1

    def count(self, text):
        for letter in text:
            self.add(letter)

    def sort(self):
        letters_array = [(k, v) for k, v in self.letters.items()]
        letters_array.sort(key=lambda x: x[1], reverse=True)
        self.sorted = letters_array

    def save(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.sorted, file)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name) as file:
            return json.load(file)


def main():
    counter = FrequencyCounter()
    counter.count_from_file('Open text.txt')
    counter.sort()
    counter.save('stat.json')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as ex:
        print("Keyboard interrupt")