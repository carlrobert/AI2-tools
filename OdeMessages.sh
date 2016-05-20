#!
# _messages.sh
# Update _messages.js based on the latest pootle translation (OdeMessages.po)
# Output: _messages.js.NEW
FILE=_messages.js
curl -LO http://pootle.appinventor.mit.edu/download/sv/app-inventor/_messages.po
curl -LOk https://github.com/mit-cml/appinventor-sources/raw/master/appinventor/blocklyeditor/src/msg/sv/$FILE

# Disassemble into constituent parts: preamble, body, postamble
python3 js2prop.py $FILE

# Process the body containing the messages subject to translation
po2prop -t 2-$FILE.properties --personality=java-utf8 _messages.po | python3 prop2js.py > 2-$FILE.properties.NEW

# Reassemble
cat 1-pre-$FILE 2-$FILE.properties.NEW 3-post-$FILE > $FILE.NEW
