import os
srcdir = '../src/'
#os.remove(srcdir+"index.md")
l = os.listdir(srcdir)
l.sort()
with open(srcdir+"index.md", mode='w', encoding="utf-8") as f:
    for i in l:
        if (i[:4] != "test"):
            f.write('* ['+i+']('+i+')\n\n')
#print("pandoc -r markdown "+srcdir+"index.md -w html -o "+srcdir+"index.html")
os.system("pandoc -r markdown "+srcdir+"index.md -w html -o "+srcdir+"index.html")
os.remove(srcdir+"index.md")
