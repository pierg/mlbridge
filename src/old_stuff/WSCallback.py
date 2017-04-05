import thread
import time
from IWSCallback import IWSCallback
from Utility import Utility


import sys, select, termios, tty

msg = """
Control Your Turtlebot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly

CTRL-C to quit
"""


def getKeyFromKeyboard():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [])
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


class WSCallback:

    def on_open(self, ws):
        print "### opened ###"
        # ws.send(Utility.constructROSJSONString("advertise", "turtlebot_command_key", "std_msgs/String"))
        # print "advertise sent"

        def run(*args):
            time.sleep(2)
            ws.send(Utility.getAdvertiseString("turtlebot_command_key", "std_msgs/String"))
            # print "advertise sent thread"
            # time.sleep(2)
            try:
                print msg
                while (1):
                    key = getKeyFromKeyboard()
                    if key == 'q':
                        break

                    print "pubKey_1: " + str(key)
                    if key != '':
                        ws.send(Utility.getPublishString("turtlebot_command_key", key))

            except KeyboardInterrupt:
                print "Keyboard Interrupt"
                pass

        thread.start_new_thread(run, ())


    def on_message(self, ws, message):
        print "### message ###"
        print message

    def on_error(self, ws, error):
        print "### error ###"
        print error

    def on_close(self, ws):
        print "### closed ###"


IWSCallback.register(WSCallback)