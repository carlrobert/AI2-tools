#  -*- coding: utf-8 -*-
# prop2js.py: App Inventor 2 (AI2) translation helper
# Converts a properties file into a .js snippet suitable for AI2
# Concatenate the preamble, the output from this script and the postamble to recover a usable .js file
# 
# The properties are represented as assignment in the .js file:
#     Blockly.Msg.LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = "parvis uppslagning  nyckel %1 par %2 hittadesInte %3"
#
# In the .properties file this corresponds to
#     Blockly.Msg.LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = parvis uppslagning  nyckel %1 par %2 hittadesInte %3
#
# See https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/blocklyeditor/src/msg/sv/_messages.js
# Thanks to https://jis.qyv.name/ for helping out

import re, sys

def quote(s):
    return s.replace('"', '\\"')

def main():
    p = re.compile(r'(Blockly[^\s]+\s=\s)(.*)', re.IGNORECASE)
    for line in sys.stdin:
        m = p.search(line)
        print('    ' + m.group(1) + '"' + quote(m.group(2)) + '"')

if __name__ == "__main__":
    main()
