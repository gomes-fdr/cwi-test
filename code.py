#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
# Não poderia ter usado estes módulos, ratiei!

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

