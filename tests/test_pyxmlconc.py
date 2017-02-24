#!/usr/bin/python
"""Testing for PyXMLConc."""
# -*- coding: utf-8 -*-
import unittest
from PySide.QtGui import *
from PySide.QtCore import *
import sys
import os
sys.path.append(os.path.abspath('../'))
from pyxmlconc.pyxmlconc import MainWindow


class BasicTestCases(unittest.TestCase):
    """Basic tests."""

    def test_basic_text_manipulation(self):
        """Basic text manipulation tests."""
        self.app = QApplication(sys.argv)
        self.test_object = MainWindow()

        self.assertEqual(self.test_object.trim_string(
                         'Fairly Long String', 10), 'ly Long St')

        self.assertEqual(self.test_object.strip_tags(
                         '<h1 att="True">Test</h1>'), 'Test')

if __name__ == '__main__':
    unittest.main()
