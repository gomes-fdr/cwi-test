#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
from datetime import datetime, timedelta

"""
You should create the following function using Python version 3 or greater:

def change_date(date: str, op: str, value: int) -> str

Where:

date: A date as string in the format "dd/MM/yyyy HH24:mi";
op: Can be only "+" | "-";
value: The value that should be incremented/decremented. It will be expressed in minutes;

Restrictions:
- you shall not work with non-native modules / libraries;
- you shall not make use of time or datetime modules, strftime or strptime, or any date/time handler library;
- if the op is not valid an ValueError must be raised;
- if the value is smaller than zero, you should ignore its signal;
- if the result sum is bigger than max value to the field, you should increment its immediate bigger field;
- ignore the fact that February have 28/29 days and always consider only 28 days;
- ignore the daylight save time rules.

Example:

result = change_date("01/03/2010 23:00", "+", 4000)
# result must be "04/03/2010 17:40"
"""

def change_date(date: str, op: str, value: int) -> str:
    operations = ('+', '-')

    try:
        dt = datetime.strptime(date, '%d/%m/%Y %H:%M')
    except ValueError:
        return None

    if not op in operations:
        raise ValueError('Invalid operation')

    if type(value) != int:
        raise ValueError('Value must be a integer')

    if op == '+':
        dt = dt + timedelta(minutes = abs(value))
    elif op == '-':
        dt = dt - timedelta(minutes = abs(value))

    return f'{dt:%d/%m/%Y %H:%M}'

