import requests
import json

def get_id(self):
    # GET ID ENDPOINT
    baseUrl = "http://localhost"
    getUrl = baseUrl + "/connectionId/id"
    requestId = requests.get(getUrl)

    if requestId.ok:
        convert_id = json.loads(requestId.text)
        print("response from get id: ", convert_id)

        return convert_id["id"]
    else:
        return -1

def reqyest_setId():
    baseUrl = "http://localhost"
    setIdUrl = baseUrl + "/connectionId/set_id"
    data = {
        'widget_id': 3,
        'widget_name': 'name'
    }
    request_setId = requests.post(url=setIdUrl, json=data)
    print(2000000000)
    if request_setId.ok:
        response = json.loads(request_setId.text)
        print('response from set id: ', response)
    else:
        print(request_setId.text) #TEXT/HTML
        print(request_setId.status_code, request_setId.reason) #HTTP
        print('dead')

def add_connection(widget_id, slot, connectionid):
    baseUrl = "http://localhost"
    addConUrl = baseUrl + "/connectionDict/add"
    data = {
        'widget_id': widget_id,
        'slot': slot,
        'connectionid': connectionid
    }
    request_addCon = requests.post(url=addConUrl, json=data)

    if request_addCon.ok:
        response = json.loads(request_addCon.text)
        print('response from add connection: ', response)

        return True
    else:
        print(request_addCon.text) #TEXT/HTML
        print(request_addCon.status_code, request_addCon.reason) #HTTP
        print('dead')
        return False
    
# add_connection(2, "slot", 3)

def remove_connection(widget_id, slot, connectionid):
    baseUrl = "http://localhost"
    removeConUrl = baseUrl + "/connectionDict/delete"
    PARAMS = {
        'widget_id': widget_id,
        'slot': slot,
        'connectionid': connectionid
    }

    request_removeCon = requests.get(url=removeConUrl, params=PARAMS)

    # TODO: update more clear debug information
    if request_removeCon.ok:
        response = json.loads(request_removeCon.text)
        print('response from add connection: ', response)

        return True
    else:
        print(request_removeCon.text) #TEXT/HTML
        print(request_removeCon.status_code, request_removeCon.reason) #HTTP
        print('dead')
        return False

# remove_connection(2, "slot", 3)

def requestIsConnected(widget_id, slot, connectionid):
    # I do not expect connectionid to be None
    # NEED further tests for this specific reason
    baseUrl = "http://localhost"
    isConnectedUrl = baseUrl + "/connectionDict/isConnected"
    PARAMS = {
        'widget_id': widget_id,
        'slot': slot,
        'connectionid': connectionid
    }
    request_isConnected = requests.get(url=isConnectedUrl, params=PARAMS)
    # TODO: update more clear debug information
    # TODO: how to make sure that boolean works
    if request_isConnected.ok:
        response = json.loads(request_isConnected.text)
        print('response from isConnection: ', response)

        if response["is_connect"] is True:
            print("true")
            return True
        else:
            print("false")
            return False
    else:
        print(request_isConnected.text) #TEXT/HTML
        print(request_isConnected.status_code, request_isConnected.reason) #HTTP
        print('dead')
        return False

# requestIsConnected(2, "slot", 3)

def requestIsSet(widget_id, slot):
    # I do not expect connectionid to be None
    # NEED further tests for this specific reason
    baseUrl = "http://localhost"
    isSetUrl = baseUrl + "/connectionDict/isSet"
    PARAMS = {
        'widget_id': widget_id,
        'slot': slot,
    }
    request_isSet = requests.get(url=isSetUrl, params=PARAMS)
    # TODO: update more clear debug information
    # TODO: how to make sure that boolean works
    if request_isSet.ok:
        response = json.loads(request_isSet.text)
        print('response from isSet: ', response)

        if response["is_set"] is True:
            print("true")
            return True
        else:
            print("false")
            return False
    else:
        print(request_isSet.text) #TEXT/HTML
        print(request_isSet.status_code, request_isSet.reason) #HTTP
        return False

requestIsSet(2, "slot")