#!/usr/bin/python
"""The main module of PyXMLConc."""
# -*- coding: utf-8 -*-
import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from bs4 import BeautifulSoup
from pyxmlconc.gui.mainwindow import Ui_MainWindow
import regex as re
from nltk.tokenize import SpaceTokenizer
from nltk.probability import FreqDist


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
        self.working_mode_box.currentIndexChanged.connect(
            self.change_working_mode_status)
        self.search_button.clicked.connect(self.search)
        self.file_name = None
        self.attributes = None
        self.search_button.setEnabled(False)
        self.save_button.setEnabled(False)
        self.tag_deselect_button.setEnabled(False)
        self.attribute_search.setEnabled(False)
        self.allow_overlap_box.setEnabled(False)

    def load_file(self):
        """Loading an XML file."""
        self.clear_concordances()
        self.file_name = QFileDialog.getOpenFileName(self, 'Open Corpus',
                                                     '../data',
                                                     ('Corpus (*.txt *.xml)'))
        self.file = open(self.file_name[0], 'r')

        with open(self.file_name[0], 'r') as file:
            self.file = file.read().replace('\n', '').replace('\r', '')

        self.find_tags()
        self.write_freqdist(self.get_frequency_distribution())

        self.attributes = self.get_attributes()
        self.search_button.setEnabled(True)
        self.save_button.setEnabled(True)

    def regex_findall_concordances(self, lr_bound, search_term, tag, ignore_case, file):
        """Calculate concordances by using regular expressions."""
        if ignore_case:
            if tag is not None:
                regexp = re.compile('(.{0,%s})(<%s>%s</%s>|<%s.*?>%s</%s>)(.{0,%s})' % (
                    lr_bound, tag, search_term, tag, tag, search_term, tag, lr_bound), re.I)
            else:
                regexp = re.compile('(.{0,%s})(%s)(.{0,%s})' % (
                    lr_bound, search_term, lr_bound), re.I)
        else:
            if tag is not None:
                regexp = re.compile('(.{0,%s})(<%s>%s</%s>|<%s.*?>%s</%s>)(.{0,%s})' % (
                    lr_bound, tag, search_term, tag, tag, search_term, tag, lr_bound))
            else:
                regexp = re.compile('(.{0,%s})(%s)(.{0,%s})' % (
                    lr_bound, search_term, lr_bound))

        return(regexp.findall(file, overlapped=self.allow_overlap_box.checkState()))

    def tokenizer_concordances(self, lr_bound, search_term, tag, ignore_case, ignore_tags, file):
        """Calculate concordances based on tokens."""
        if ignore_tags:
            tokens = SpaceTokenizer().tokenize(self.strip_tags(file))
        else:
            file = re.sub(r'<.*?>', self.sanitize_tags_for_tokenizer, file)
            tokens = SpaceTokenizer().tokenize(file)

        if ignore_case:
            if tag is not None:
                regexp = re.compile('(<%s>%s</%s>|<%s.*?>%s</%s>)' % (
                    tag, search_term, tag, tag, search_term, tag), re.I)
            else:
                regexp = re.compile(search_term, re.I)
        else:
            if tag is not None:
                regexp = re.compile('(<%s>%s</%s>|<%s.*?>%s</%s>)' % (
                    tag, search_term, tag, tag, search_term, tag))
            else:
                regexp = re.compile(search_term)

        concordances = []

        print(concordances)

        for i in range(len(tokens)):
            if regexp.match(tokens[i]):
                boundaries = self.generate_boundaries(lr_bound, tokens, i)
                concordances.append((boundaries[0], tokens[i], boundaries[1]))

        return concordances

    def generate_boundaries(self, lr_bound, tokens, pos):
        """Generating the sourrunding context."""
        left_boundary = []
        right_boundary = []

        for i in reversed(range(lr_bound)):
            i += 1

            try:
                left_boundary.append(tokens[pos - i])
            except IndexError:
                pass

            try:
                right_boundary.append(tokens[pos + i])
            except IndexError:
                pass

        left_boundary = " ".join(left_boundary)
        right_boundary = " ".join(reversed(right_boundary))

        return((left_boundary, right_boundary))

    def find_concordances(self):
        """Finding concordances."""
        self.clear_concordances()
        search_term = self.search_bar.text()
        lr_bound = self.lrbound.value()
        ignore_case = self.ignore_case_box.checkState()
        ignore_tags = self.ignore_tags_box.checkState()
        working_mode = self.working_mode_box.currentText()

        try:
            tag = self.tag_list.currentItem().text()
        except AttributeError:
            tag = None

        if self.ignore_tags_box.checkState():
            file = self.strip_tags(self.file)
        else:
            file = self.file

        if working_mode == 'Tokenizer':
            concordances = self.tokenizer_concordances(
                lr_bound, search_term, tag, ignore_case, ignore_tags, file)
        else:
            concordances = self.regex_findall_concordances(
                lr_bound, search_term, tag, ignore_case, file)

        # Look for Attributes
        if self.attribute_search.text():
            concordances_filtered = []
            attributes_values = self.attribute_search.text().split(';')
            for attribute_value in attributes_values:
                for concordance in concordances:
                    if attribute_value in concordance[1]:
                        concordances_filtered.append(concordance)

            concordances = concordances_filtered

        # Writing the Concordances
        if len(concordances) > 0:
            self.results_label.setText('%s Results' % len(concordances))

            max_len = max_len = len(search_term) + lr_bound * 2

            just = 0
            for string in max(concordances, key=len):
                just += len(string)

            for concordance in concordances:
                if self.strip_tags_box.checkState():
                    concordance = list(map(self.strip_tags, concordance))
                    print(concordance)

                if working_mode == 'Tokenizer':
                    concordance = '%s    %s    %s' % (concordance[0].rjust(
                        just), concordance[1], concordance[2].ljust(just))
                else:
                    concordance = self.trim_string('%s    %s    %s' %
                                                   (concordance[0].rjust(
                                                    self.lrbound.value()),
                                                    concordance[1],
                                                    concordance[2].ljust(
                                                        self.lrbound.value())),
                                                   max_len)

                item = QListWidgetItem(concordance)
                item.setTextAlignment(Qt.AlignHCenter)
                self.concordance_list.addItem(item)
        else:
            item = QListWidgetItem('Nothing found!')
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
        """Clearing the concordances list."""
        while(self.concordance_list.count() > 0):
            self.concordance_list.takeItem(0)

    def clear_tags(self):
        """Clearing the tags list."""
        while(self.tag_list.count() > 0):
            self.tag_list.takeItem(0)

    def clear_frequencies(self):
        """Clearing the frequencies list."""
        while(self.frequency_list.count() > 0):
            self.frequency_list.takeItem(0)

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
        soup = BeautifulSoup(string, 'lxml')
        return (soup.get_text())

    def sanitize_tags_for_tokenizer(self, match):
        """Replacing spaces in tags to prevent the tokenizer from splitting."""
        print(match, match[0].replace(' ', '_'))
        return match[0].replace(' ', '_')

    def search(self):
        """Finding the concordances and enable the save button."""
        if self.search_bar.text().rstrip('\r\n') != '':
            self.find_concordances()
            self.save_button.setEnabled(True)
            self.set_scrollbar()
        else:
            self.message_box('Please provide a search term!')

    def set_scrollbar(self):
        """Setting the scrollbar to the middle."""
        self.concordance_list.horizontalScrollBar().setValue(
            self.concordance_list.horizontalScrollBar().maximum() / 2)

    def change_tag_status(self):
        """Enabling the tag search function."""
        if self.ignore_tags_box.checkState():
            self.tag_deselect_button.setEnabled(False)
            self.attribute_search.setEnabled(False)
            self.tag_list.setEnabled(False)
            self.deselect_tags()
        else:
            self.tag_list.setEnabled(True)

    def change_working_mode_status(self):
        """Enabling allow overlap function if working mode is re.findall."""
        if self.working_mode_box.currentText() == 're.findall':
            self.allow_overlap_box.setEnabled(True)
        else:
            self.allow_overlap_box.setEnabled(False)

    def message_box(self, message):
        """Showing a message box."""
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.exec_()

    def get_frequency_distribution(self):
        """Generating the frequency distribution."""
        tokens = SpaceTokenizer().tokenize(self.strip_tags(self.file))
        return(FreqDist(tokens))

    def write_freqdist(self, freqdist):
        """Populating the frequency list."""
        self.clear_frequencies()
        for freq in freqdist:
            item = QListWidgetItem('%s : %s' % (freq, freqdist[freq]))
            self.frequency_list.addItem(item)


def main():
    """The main function that starts the GUI."""
    app = QApplication(sys.argv)
    main_window = MainWindow()
    ret = app.exec_()
    sys.exit(ret)


if __name__ == '__main__':
    main()
