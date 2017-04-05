import websocket
import thread

class WSClient:

    def __init__(self, address, port, iwscallback):
        self.address = address
        self.port = port
        self.iwscallback = iwscallback

    # def connect_newthread(self):
    #     def run(*args):
    #         websocket.enableTrace(True)
    #         address_and_port = "ws://" + self.address + ":" + self.port
    #         self.ws = websocket.WebSocketApp(address_and_port,
    #                                          on_message=self.iwscallback.on_message,
    #                                          on_error=self.iwscallback.on_error,
    #                                          on_close=self.iwscallback.on_close)
    #         self.ws.on_open = self.iwscallback.on_open
    #         self.ws.run_forever()
    #     thread.start_new_thread(run, ())

    def connect(self):
        websocket.enableTrace(True)
        address_and_port = "ws://" + self.address + ":" + self.port
        self.ws = websocket.WebSocketApp(address_and_port,
                                         on_message=self.iwscallback.on_message,
                                         on_error=self.iwscallback.on_error,
                                         on_close=self.iwscallback.on_close)
        self.ws.on_open = self.iwscallback.on_open
        self.ws.run_forever()

    def send_newthread(self, message):
        def run(*args):
            self.ws.send(message)
        thread.start_new_thread(run, ())

    def send(self, message):
        self.ws.send(message)

    def close(self):
        self.ws.close()

