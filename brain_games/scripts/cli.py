
# coding: utf-8
import prompt


def hello():
    name = prompt.string('May I have your name?')
    print('Hello, {}!'.format(name))
