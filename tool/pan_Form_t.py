import sys
import os

HEAD ="""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../../css/article.css">
    <script type="text/javascript" src="../../js/setHead.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
    <title>FIDT电台</title>
</head>
<body>
    <iframe id="head"></iframe><script>setTTHead()</script>
"""

REAR ="""
</body>
</html>"""

def main(argv):
    os.system("pandoc -r markdown -w html {} -o {}.html".format(argv[1], argv[1][:-3]))
    f = open(argv[1][:-3]+".html", 'r+', encoding="utf-8")
    content = f.read()
    f.seek(0)
    f.write(HEAD+content+REAR)
    f.close()
    
if __name__ == "__main__":
    main(sys.argv)
