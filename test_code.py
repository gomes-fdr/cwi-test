#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
from code import change_date

class TestChangeDate(TestCase):

    def test_is_invalid_date(self):
        self.assertIsNone(change_date('bla bla', 'bla', 0))

    def test_is_invalid_op(self):
        with self.assertRaises(ValueError): change_date('24/05/1974 06:30', 'bla', 0)

    def test_is_invalid_value(self):
        with self.assertRaises(ValueError): change_date('24/05/1974 06:30', '+', 'w')

    def test_is_valid_value_less_zero(self):
        self.assertEqual(change_date('01/03/2010 23:00', '+', -4000), '04/03/2010 17:40')

    def test_valid_date_sum(self):
        self.assertEqual(change_date('01/03/2010 23:00', '+', 4000), '04/03/2010 17:40')

    def test_valid_date_sub(self):
        self.assertEqual(change_date('04/03/2010 17:40', '-', 4000), '01/03/2010 23:00')

if __name__ == '__main__':
    main()