#link = https://www.dataquest.io/blog/python-api-tutorial/

import json
import requests
resData = None
def callGmAPI(id, param):
    if param is None:
        parameters = {'id': id, 'responseType': 'JSON'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://gmapi.azurewebsites.net/getVehicleInfoService", data=json.dumps(parameters), headers=headers)
        data = response.json()
        vin = data['data']['vin']['value']
        color = data['data']['color']['value']
        if data['data']['fourDoorSedan']['value'] == 'True':
            doorCount = '4'
        else:
            doorCount = '2'
        driveTrain = data['data']['driveTrain']['value']
        resData = {'vin': vin, 'color': color, 'doorCount': doorCount, 'driveTrain': driveTrain}

    elif param == 'doors':
        parameters = {'id': id, 'responseType': 'JSON'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://gmapi.azurewebsites.net/getSecurityStatusService", data=json.dumps(parameters),headers=headers)
        data = response.json()
        doors = data['data']['doors']['values']
        resData = []
        for door in doors:
            tempDict = {'location': door['location']['value'], 'locked': door['locked']['value']}
            resData.append(tempDict)

    elif param == 'fuel':
        parameters = {'id': id, 'responseType': 'JSON'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://gmapi.azurewebsites.net/getEnergyService", data=json.dumps(parameters), headers=headers)
        data = response.json()
        percent = data['data']['tankLevel']['value']
        resData = {'percent': percent}

    elif param == 'battery':
        parameters = {'id': id, 'responseType': 'JSON'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post("http://gmapi.azurewebsites.net/getEnergyService", data=json.dumps(parameters), headers=headers)
        data = response.json()
        percent = data['data']['batteryLevel']['value']
        resData = {'percent': percent}

    resDataJson = json.loads(json.dumps(resData))
    return resDataJson

def callGmAPIPost(id, request):
    if request.data['action'] == 'START': command = 'START_VEHICLE'
    else: command = 'STOP_VEHICLE'
    parameters = {'id': id, 'command': command, 'responseType': 'JSON'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post("http://gmapi.azurewebsites.net/actionEngineService", data=json.dumps(parameters), headers=headers)
    data = response.json()
    res = {'status': data['actionResult']['status']}
    return res
