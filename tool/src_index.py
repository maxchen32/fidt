import os
srcdir = '../src/'

f = open(srcdir+"toc.html", mode='w', encoding="utf-8")

l = os.listdir(srcdir)
l.sort()
l.remove("toc.html")
l.remove("head.html")
l.remove("index.html")

HEAD = """<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../css/homepage.css" />
    <script type="text/javascript" src="../js/viewLink.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
</head>
<body onload="viewLink()" style="background-color: #ddffff;">
<ul>"""
REAR = """</ul>
</body>
</html>"""

f.write(HEAD)
for i in l:
	if (i[:4] != "test" and i[:3] != "tmp"):
		f.write('<li><a href="' +i+ '" class="uri">' +i+ '</a></li> <br />\n')
f.write(REAR)
f.close()


