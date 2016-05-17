#!
# Update OdeMessages_sv.properties based on the latest pootle translation (OdeMessages.po) 
curl -LO http://pootle.appinventor.mit.edu/download/sv/app-inventor/OdeMessages.po
curl -LOk https://github.com/mit-cml/appinventor-sources/raw/master/appinventor/appengine/src/com/google/appinventor/client/OdeMessages_sv.properties
po2prop -t OdeMessages_sv.properties --personality=java-utf8 OdeMessages.po -o OdeMessages_sv.properties.NEW
