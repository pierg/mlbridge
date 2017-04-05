import json


class Utility(object):

    @staticmethod
    def constructROSJSON(op, topic, type = '', message = ''):
        parsed_json = 0

        if op == "advertise":
            json_string = '{ "op": "' + op + '", "topic": "/' + topic + '", "type": "' + type + '" }'
            parsed_json = json.load(json_string)
        if op == "publish":
            json_string = '{ "op": "' + op + '", "topic": "/' + topic + '", "msg": "' + '{"data": "' + message + '"}' + '" }'
            parsed_json = json.load(json_string)
        if op == "subscribe":
            json_string = '{ "op": "' + op + '", "topic": "/' + topic + '", "type": "' + type + '" }'
            parsed_json = json.load(json_string)

        return parsed_json

    @staticmethod
    def getAdvertiseString(topic, type):
        return '{ "op": "' + "advertise" + '", "topic": "/' + topic + '", "type": "' + type + '" }'

    @staticmethod
    def getPublishString(topic, message):
        return '{ "op": "' + "publish" + '", "topic": "/' + topic + '", "msg": ' + '{"data": "' + message + '"}' + ' }'


