def readfile(path):
    with open(path) as file:
        data = file.read()
    return data

def indent(text,levels=1,width=4,firstline=False):
    indent = ' ' * width * levels
    if firstline:
        text = indent + text
    return text.replace('\n', '\n' + indent)

BOILERPLATE='''<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="manifest" href="site.webmanifest" />
<script>navigator.serviceWorker.register("/service-worker.js");</script>
''' + readfile("assets/icons/icons.html") + '''

''' + '''

'''


TS='type="text/typescript"'
TSMODULE='type="tsmodule"'
LESS='type="text/less"'