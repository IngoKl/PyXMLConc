# PyXMLConc

![PyXMLConc-Logo](https://user-images.githubusercontent.com/16179317/100772813-5e335980-3400-11eb-909c-9a306bce3153.png)

PyXMLConc is a very simple concordancer. It is supposed to be used in exploratory analysis of XML-annotated corpora. Its primary feature lies in the automatic detection of XML tags and attributes. The search/concordancing function supports regular expressions.

**Note:** Please be aware that this is *not* production software/code at all. I primarily use this tool to teach XML annotated corpora. There are numerous bugs and idiosyncrasies.

## Usage

After cloning the repository, simply run `python -m pyxmlconc.pyxmlconc`. 
Alternatively, you can install PyXMLConc by running `pip install .`. This will make `PyXMLConc` available as a shell command.

The concordancer supports two working modes. The default mode (**Tokenizer**) tokenizes the text and builds the concordances from the individual tokens. The second mode, **re.findall**, uses regular expressions to search the text without previous tokenization. While this mode is somewhat more flexible, the user has to account for potential overlaps resulting in 'missing' concordances.

## Todo

- Add additional tests
- Automatically centering the scrollbar
- Frequency table as an actual table
- Allow search from the frequency table
- Color the actual search term; split up the concordance into columns
- Read possible attributes
- Select search terms from the frequency list
- Fix issues when there are multiple attributes

## Screenshot

![Screenshot](https://cloud.githubusercontent.com/assets/16179317/23309280/516f3366-faae-11e6-9af6-4403f24aac1f.png?raw=true)

## Updates

    * (2020-12-01) PyXMLConc 0.2 - Upgrade to Qt 5 and PySide2; Add simple frequency tables
