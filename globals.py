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
<script>
    (async function() {
        let serviceWorker = null;
        if ('serviceWorker' in navigator) {
            try {
                const registration = await navigator.serviceWorker.register("/service-worker.js");

                serviceWorker = registration.installing
                                ?? registration.waiting
                                ?? registration.active
                                ?? null;

                if (serviceWorker) {
                    const logServiceWorkerState = () => console.log('Service Worker State: ' + serviceWorker.state);
                    logServiceWorkerState();
                    serviceWorker.addEventListener("statechange", event => logServiceWorkerState());
                } else {
                    throw new Error('Service Worker is null');
                }
            } catch(error) {
                console.error('Error installing Service Worker: ' + e);
            }
        } else {
            console.error('Error installing Service Worker: ' + 'Service Workers are not supported');
        }

        window.serviceWorker = serviceWorker;
    })();
</script>
''' + readfile("assets/icons/icons.html") + '''

''' + '''

'''


TS='type="text/typescript"'
TSMODULE='type="tsmodule"'
LESS='type="text/less"'