from WSClient import WSClient
from WSCallback import WSCallback

if __name__ == "__main__":

    adress = "192.168.1.142"
    port = "9090"
    wscallback = WSCallback()
    wsclient = WSClient(adress, port, wscallback)

    wsclient.connect()

    print "connected?"

    # wsclient.send("CIAO")

    print "CIAO?"


