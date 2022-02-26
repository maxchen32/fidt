import sys
import os

HEAD ="""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../css/article.css">
    <link rel="stylesheet" type="text/css" href="../css/marx.min.css">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
    <title>FIDT电台</title>
</head>
<body>
    <div>
            <a href="https://maxchen32.github.io/fidt" title="FIDT-&#x9996;&#x9875;">
                    <img src="../pic/logo.png" alt="FIDT_logo" height="200" width="200">
            </a><br>
            <strong style="color: red">&#x672C;&#x9875;&#x9762;&#x4EC5;&#x4E3A;&#x73A9;&#x7B11;&#xFF0C;&#x5E76;&#x65E0;&#x6076;&#x610F;</strong><br>
    </div>
<main>
    
"""

REAR ="""
</main>
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
