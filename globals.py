def readfile(path):
    with open(path) as file:
        data = file.read()
    return data

def indent(text,levels=1,width=4,firstline=False):
    indent = ' ' * width * levels
    if firstline:
        text = indent + text
    return text.replace('\n', '\n' + indent)

BOILERPLATE=readfile("assets/icons/icons.html")+readfile('boilerplate.html')


TS='type="text/typescript"'
TSMODULE='type="tsmodule"'
LESS='type="text/less"'