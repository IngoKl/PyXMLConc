#!/usr/bin/python
"""The main module of PyXMLConc."""
# -*- coding: utf-8 -*-
import sys
from PySide.QtGui import *
from PySide.QtCore import *
from bs4 import BeautifulSoup
from gui.mainwindow import Ui_MainWindow
import re


def lolz():
    return "lol"


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main GUI window."""

    def __init__(self):
        """Initializing the GUI."""
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.load_button.clicked.connect(self.load_file)
        self.save_button.clicked.connect(self.save_file)
        self.tag_deselect_button.clicked.connect(self.deselect_tags)
        self.tag_list.itemClicked.connect(self.show_attributes)
        self.ignore_tags_box.stateChanged.connect(self.change_tag_status)
        self.search_button.clicked.connect(self.search)
        self.file_name = None
        self.attributes = None
        self.search_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.tag_deselect_button.setEnabled(False)
        self.attribute_search.setEnabled(False)

    def load_file(self):
        """Loading an XML file."""
        self.clear_concordances()
        self.file_name = QFileDialog.getOpenFileName(self)
        self.file = open(self.file_name[0], 'r')

        with open(self.file_name[0], 'r') as file:
            self.file = file.read().replace('\n', '').replace('\r', '')

        self.find_tags()
        self.attributes = self.get_attributes()
        self.search_button.setEnabled(True)
        self.save_button.setEnabled(True)

    def find_concordances(self):
        """Finding concordances."""
        self.clear_concordances()
        lr_bound = self.lrbound.value()
        search_term = self.search_bar.text()

        if self.ignore_case_box.checkState():
            try:
                tag = self.tag_list.currentItem().text()
                regexp = re.compile('(.{0,%s})(<%s>%s</%s>|<%s.*?>%s</%s>)(.{0,%s})' % (
                    lr_bound, tag, search_term, tag, tag, search_term, tag, lr_bound), re.I)
            except AttributeError:
                regexp = re.compile('(.{0,%s})(%s)(.{0,%s})' % (
                    lr_bound, search_term, lr_bound), re.I)
        else:
            try:
                tag = self.tag_list.currentItem().text()
                regexp = re.compile('(.{0,%s})(<%s>%s</%s>|<%s.*?>%s</%s>)(.{0,%s})' % (
                    lr_bound, tag, search_term, tag, tag, search_term, tag, lr_bound))
            except AttributeError:
                regexp = re.compile('(.{0,%s})(%s)(.{0,%s})' % (
                    lr_bound, search_term, lr_bound))

        if self.ignore_tags_box.checkState():
            concordances = regexp.findall(self.strip_tags(self.file))
        else:
            concordances = regexp.findall(self.file)

        # Look for Attributes
        if self.attribute_search.text():
            concordances_filtered = []
            attributes_values = self.attribute_search.text().split(';')
            for attribute_value in attributes_values:
                for concordance in concordances:
                    print attribute_value
                    print concordance[1]
                    if attribute_value in concordance[1]:
                        concordances_filtered.append(concordance)

            concordances = concordances_filtered

        for concordance in concordances:
            if self.strip_tags_box.checkState():
                concordance = map(self.strip_tags, concordance)

            max_len = len(search_term) + lr_bound * 2
            concordance = self.trim_string(
                '%s    %s    %s' %
                (concordance[0].rjust(
                    self.lrbound.value()), concordance[1], concordance[2].ljust(
                    self.lrbound.value())), max_len)

            item = QListWidgetItem(concordance)
            item.setTextAlignment(Qt.AlignHCenter)
            self.concordance_list.addItem(item)

    def get_attributes(self):
        """Generating a dictionary of tags and possible/existing attributes."""
        attributes = {}
        soup = BeautifulSoup(self.file, 'html.parser')
        for elm in soup():
            if elm.name in attributes.keys():
                attributes[elm.name] += list(elm.attrs)
            else:
                attributes[elm.name] = list(elm.attrs)

        for tag in attributes:
            attributes[tag] = list(set(attributes[tag]))

        return attributes

    def show_attributes(self):
        """Presenting the user with all possible attributes of a tag."""
        tag = self.tag_list.currentItem().text()
        self.statusBar.showMessage('Attributes for "%s": %s' % (
            tag, ', '.join(self.attributes[tag])))

        self.tag_deselect_button.setEnabled(True)
        self.attribute_search.setEnabled(True)

    def find_tags(self):
        """Finding all available tags."""
        self.clear_tags()
        soup = BeautifulSoup(self.file, 'html.parser')
        tags = list(set([tag.name for tag in soup.find_all()]))

        for tag in tags:
            self.tag_list.addItem(tag)

    def clear_concordances(self):
        """Clearing the concordances windows."""
        while(self.concordance_list.count() > 0):
            self.concordance_list.takeItem(0)

    def clear_tags(self):
        """Clearing the tags windows."""
        while(self.tag_list.count() > 0):
            self.tag_list.takeItem(0)

    def deselect_tags(self):
        """Deselecting all tags."""
        self.tag_list.clearSelection()
        self.tag_list.setCurrentItem(None)
        self.tag_deselect_button.setEnabled(False)
        self.attribute_search.setEnabled(False)

    def save_file(self):
        """Saving the current concordances window."""
        save_file_name = QFileDialog.getSaveFileName(self)[0]

        if len(save_file_name) > 0:
            with open(save_file_name, 'w') as save_file:
                for i in xrange(self.concordance_list.count()):
                    save_file.write(''.join(
                                    [str(self.concordance_list.item(i).text()
                                         ), '\n']))

    def trim_string(self, string, length):
        """Trimming a string to a given length."""
        if len(string) > length:
            too_long_per_side = abs((length - len(string)) / 2)
            return(string[too_long_per_side:-too_long_per_side])
        else:
            return string

    def strip_tags(self, string):
        """Stripping all tags and attributes from a string."""
        soup = BeautifulSoup(string)
        return (soup.get_text())

    def search(self):
        """Finding the concordances and enable the save button."""
        self.find_concordances()
        self.save_button.setEnabled(True)

    def change_tag_status(self):
        """Enabling the tag search function."""
        if self.ignore_tags_box.checkState():
            self.tag_deselect_button.setEnabled(False)
            self.attribute_search.setEnabled(False)
            self.tag_list.setEnabled(False)
        else:
            self.tag_list.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit(ret)
