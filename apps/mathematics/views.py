import random

from flask import render_template

from . import main

MIN_VALUE = 5
MAX_VALUE = 20


@main.route('/add', methods=['GET'], endpoint='math_add')
def add():
    while True:
        num1 = random.randint(MIN_VALUE, MAX_VALUE)
        num2 = random.randint(MIN_VALUE, MAX_VALUE)
        if num1 + num2 < 20:
            break

    return render_template('mathematics/add.html', num1=num1, num2=num2)


@main.route('/sub', methods=['GET'], endpoint='math_sub')
def sub():
    while True:
        num1 = random.randint(MIN_VALUE, MAX_VALUE)
        num2 = random.randint(MIN_VALUE, MAX_VALUE)
        if num1 > num2:
            break

    return render_template('mathematics/sub.html', num1=num1, num2=num2)
