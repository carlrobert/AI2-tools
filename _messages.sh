#!
# _messages.sh
# Update _messages.po based on the latest pootle translation (OdeMessages.po) 
curl -LO http://pootle.appinventor.mit.edu/download/sv/app-inventor/_messages.po
curl -LOk https://github.com/mit-cml/appinventor-sources/raw/master/appinventor/blocklyeditor/src/msg/sv/_messages.js
python js2prop.py _messages.js
po2prop -t 2-prop.properties --personality=java-utf8 _messages.po -o 2-prop.properties.NEW
cat 1-preamble-* 2-prop.NEW 3-postamble- > _messages.js.NEW
