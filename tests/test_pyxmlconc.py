#!/usr/bin/python
"""Testing for PyXMLConc."""
# -*- coding: utf-8 -*-

import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import QApplication
from pyxmlconc.pyxmlconc import MainWindow

app = QApplication(sys.argv)
main_window = MainWindow()


def test_strip_tags():
    """Test strip_tags."""
    assert(main_window.strip_tags('<h1 att="True">Test</h1>')) == 'Test'
    assert(main_window.strip_tags('<w c5="VVZ" hw="provide" pos="VERB">provides</w>')) == 'provides'


def test_trim_string():
    """Test trim_strings."""
    assert(main_window.trim_string('Fairly Long String', 10)) == 'ly Long St'
