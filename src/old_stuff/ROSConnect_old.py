import websocket
import thread
import time
from Utility import Utility

import json


def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    print "### opening...###"
    def run(*args):
        ws.send(Utility.constructROSJSONString("advertise", "turtlebot_command_key", "std_msgs/String"))
        print "advertise sent thread"
        # time.sleep(1)
        # ws.send(Utility.constructROSJSONString("publish", "turtlebot_command_key", "k"))
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.1.142:9090",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()
