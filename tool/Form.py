f = open("tmp.html", 'w', encoding="utf-8")
print("input title:")
title = input()
print("input picture name:")
piclink = input()

HEAD =''.join(("""<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="../css/article.css">
    <script type="text/javascript" src="../js/setHead.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
    <title>""", title,
    """</title>
</head>
<body>
    <iframe id="head"></iframe><script>setHead()</script>
    <div>
        <h1>""",title,
    """</h1>
    </div>"""))
REAR ="""
</body>
</html>"""
DIVs ="""
    <div>"""
DIVe ="""
    </div>"""
Ps = """
        <p>"""
Pe = """</p>"""
IMG = "<img class=\"txtpic\" src=\"../pic/" + piclink + "\" />"
para = DIVs + Ps + "<!--input text here-->" + "<i>&#xFF08;FIDT&#x7535;&#x53F0;&#x62A5;&#x9053;&#xFF09;</i>" + Pe + DIVe
pic = DIVs + Ps + IMG + Pe + DIVe
f.write(HEAD+pic+para+REAR)
f.close()
