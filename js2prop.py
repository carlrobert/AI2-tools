#  -*- coding: utf-8 -*-
# js2prop.py: App Inventor 2 (AI2) translation helper
# Split _messages.js into a preamble, properties file (po2prop) and postamble
# The properties file can then be used as input to po2prop
# 
# The properties are represented as assignment in the .js file:
#     Blockly.Msg.LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = "parvis uppslagning  nyckel %1 par %2 hittadesInte %3"
#
# In the .properties file this corresponds to
#     LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = parvis uppslagning  nyckel %1 par %2 hittadesInte %3
#
# See https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/blocklyeditor/src/msg/sv/_messages.js
# Thanks to https://jis.qyv.name/ for helping out

import re
from sys import argv

script, filename = argv
files = ['1-preamble.js', '2-prop.po', '3-postamble.js']
fileCount = 0

target = open(files[fileCount], 'w')
target.truncate()
p = re.compile(r'(Blockly[^\s]+)\s=\s(?P<quote>[\'"])(.*)(?P=quote)', re.IGNORECASE)

with open(filename, encoding='utf-8') as inf:
    for line in inf:
        m = p.search(line)
        if m and fileCount < 2:
            if fileCount == 0:
                # Switch output to .po file upon first match
                target.close()
                fileCount += 1
                target = open(files[fileCount], 'w')
                target.truncate()
            target.write(m.group(1) + ' = ' + m.group(3) + '\n')
            print(line)
        else:
            if fileCount == 1:
                # Switch to postamble upon first mismatch
                print(line)
                target.close()
                fileCount += 1
                target = open(files[fileCount], 'w')
                target.truncate()
            target.write(line)
