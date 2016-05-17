#  -*- coding: utf-8 -*-
# js2prop.py: App Inventor 2 (AI2) translation helper
# Split _messages.js into a preamble, a properties file (usable with po2prop) and a postamble
# 
# The properties are represented as assignments in the .js file:
#     Blockly.Msg.LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = "parvis uppslagning  nyckel %1 par %2 hittadesInte %3"
#
# In the .properties file this corresponds to
#     LANG_LISTS_LOOKUP_IN_PAIRS_INPUT = parvis uppslagning  nyckel %1 par %2 hittadesInte %3
#
# See https://github.com/mit-cml/appinventor-sources/blob/master/appinventor/blocklyeditor/src/msg/sv/_messages.js
# Thanks to https://jis.qyv.name/ for helping out

import re
from sys import argv

def main():
	script, filename = argv
	files = ['1-pre-' + filename, '2-' + filename + '.properties', '3-post-' + filename]
	preamble, properties, postamble = 0, 1, 2
	fileCount = 0

	target = open(files[fileCount], 'w')
	target.truncate()
	p = re.compile(r'(Blockly[^\s]+)\s=\s(?P<quote>[\'"])(.*)(?P=quote)', re.IGNORECASE)

	with open(filename, encoding='utf-8') as inf:
		for line in inf:
			if fileCount == preamble:
				m = p.search(line)
				if m:
					target.close()
					fileCount = 1
					target = open(files[fileCount], 'w')
					target.truncate()
				target.write(line)
			elif fileCount == properties:
				m = p.search(line)
				if m:
					target.write(m.group(1) + ' = ' + m.group(3) + '\n')
				else:           
					target.close()
					fileCount = 2
					target = open(files[fileCount], 'w')
					target.truncate()
					target.write(line)
			elif fileCount == postamble:
				target.write(line)
			else:
				sys.exit('Such error. Many fail')

if __name__ == "__main__":
    main()

#TODO: Make sure beginning-of-line spaces are kept
