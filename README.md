# PyXMLConc

PyXMLConc is a very simple concordancer. It is supposed to be used in exploratory analysis of XML-annotated corpora. Its primary feature lies in the automatic detection of XML tags and attributes. The search/concordancing function supports regular expressions.

## Usage
After cloning the repository, simply run `python pyxmlconc/pyxmlconc.py`. Alternatively, you can install PyXMLConc by running `pip install .`. This will make `PyXMLConc` available as a shell command.

The concordancer supports two working modes. The default mode (**Tokenizer**) tokenizes the text and builds the concordances from the individual tokens. The second mode, **re.findall**, uses regular expressions to search the text without previous tokenization. While this mode is somewhat more flexible, the user has to account for potential overlaps resulting in 'missing' concordances.

I also provide compiled/binary versions for Windows:
* [PyXMLConc-0.1](https://dev.kleiber.me/pyxmlconc/PyXMLConc-0.1.exe) ([SHA 256] e64391aabeaa42a94c4baf1c1d0dd9854f85178683e5f2ffa94d5f24b25c1536) (40mb)

## Todo
- [X] Simple frequency table
- [ ] Unit-Tests
- [ ] Automatically centering the scrollbar
- [ ] Frequency table as an actual table
- [ ] Allow search from frequency table
- [ ] Color the actual search term

## Screenshot
![Screenshot](https://cloud.githubusercontent.com/assets/16179317/23309280/516f3366-faae-11e6-9af6-4403f24aac1f.png?raw=true)
