curl -O http://pootle.appinventor.mit.edu/download/sv/app-inventor/_messages.po -L --proxy https://23048519:mn6aBoxV@proxy.global.sonyericsson.net:8080

po2prop -t 2-prop.properties --personality=java-utf8 _messages.po -o test2



